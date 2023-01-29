# Cloud Experiments
## INSTALL

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requiremnts.txt
python3 create_db.py
```
If need mysql, just run it on localhost:
```
docker run --name mysql -d \
       -p 3306:3306 \
       -e MYSQL_ROOT_PASSWORD=change-me \
       --restart unless-stopped \
       mysql:8
```

Than create database and after import initial data.
```
python3 create_db.py
```


For RabbitMQ:
```
docker run --name cld-rabbit -d \
       --hostname cld-rabbit \
       -p 5671:5671/tcp -p 5672:5672/tcp -p 15672:15672/tcp -p 15692:15692/tcp \
       --dns 8.8.8.8 \
       rabbitmq:3.11-management-alpine
```

## RUN

For generate 100 jobs run:
```
python3 generator.py 100
```

Or 100 by 100:
```
for i in `seq 100`; do python3 generator.py 100; done
```

