#!/usr/bin/env python
import pika
import sys

def send_to_mq(routing_key='anonymous.info', message='Hello World!'):
    # Connect to RMQ server
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))  #TODO remove hardcode
    channel = connection.channel()
    # Create Queue and Exchange
    exchange = 'topic_ex'
    channel.queue_declare(queue=routing_key)
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    
    channel.basic_publish(exchange=exchange, 
                          routing_key=routing_key,
                          body=message)
    print(" [x] Sent %r - %r:%r" % (exchange, routing_key, message))
    connection.close()
