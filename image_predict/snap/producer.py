

import pika
import json
params=pika.ConnectionParameters('host.docker.internal',heartbeat=60)
connection = pika.BlockingConnection(params)

channel=connection.channel()

def publish(data):
    
    channel.basic_publish(exchange='',routing_key='json.to.csv',body=json.dumps(data))
