resource "vkcs_networking_network" "k8s" {
	name = "k8s-net"
	admin_state_up = true
}

resource "vkcs_networking_subnet" "k8s-subnetwork" {
	name = "k8s-subnet"
	network_id = vkcs_networking_network.k8s.id
	cidr = "10.20.30.0/24"
	ip_version = 4
	dns_nameservers = ["8.8.8.8", "8.8.4.4"]
}

data "vkcs_networking_network" "extnet" {
	name = "ext-net"
}

resource "vkcs_networking_router" "k8s" {
	name = "k8s-router"
	admin_state_up = true
	external_network_id = data.vkcs_networking_network.extnet.id
}

resource "vkcs_networking_router_interface" "k8s" {
	router_id = vkcs_networking_router.k8s.id
	subnet_id = vkcs_networking_subnet.k8s-subnetwork.id
}

resource "vkcs_compute_keypair" "keypair" {
	name = "default"
}

data "vkcs_compute_flavor" "k8s_master" {
	name = "Standard-2-4-40"
}

data "vkcs_compute_flavor" "k8s_worker" {
	name = "Basic-1-2-20"
}

data "vkcs_kubernetes_clustertemplate" "cluster_template" {
	version = "1.21.4"
}

resource "vkcs_kubernetes_cluster" "k8s-cluster" {
	depends_on = [
		vkcs_networking_router_interface.k8s,
	]
	name = "k8s-cluster"
	cluster_template_id = data.vkcs_kubernetes_clustertemplate.cluster_template.id
	master_flavor = data.vkcs_compute_flavor.k8s_master.id
	master_count = 1
	availability_zone = "MS1"
	labels = {
		ingress_controller = "nginx"
	}
	keypair = vkcs_compute_keypair.keypair.id
	network_id = vkcs_networking_network.k8s.id
	subnet_id = vkcs_networking_subnet.k8s-subnetwork.id
	floating_ip_enabled = true
}

resource "vkcs_kubernetes_node_group" "default_ng" {
	depends_on = [
		vkcs_kubernetes_cluster.k8s-cluster,
	]
	cluster_id = vkcs_kubernetes_cluster.k8s-cluster.id
	name = "default"
	node_count = 1
	autoscaling_enabled = true
	max_nodes = 2
	min_nodes = 1
	flavor_id = data.vkcs_compute_flavor.k8s_worker.id
}

