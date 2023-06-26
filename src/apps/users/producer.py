import json

import pika
from django.conf import settings

from src.amqp import channel_factory
from src.logger import Logger


def publish(action, body):
    try:
        channel = channel_factory()
    
        channel.queue_declare(queue=settings.USERS_SERVICE_QUEUE, durable=True)

        properties = pika.BasicProperties(
            headers={'action': action},
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
        channel.basic_publish(
            exchange='',
            routing_key=settings.USERS_SERVICE_QUEUE,
            body=json.dumps(body),
            properties=properties
        )
        Logger.info(f"Published message {action} to {settings.USERS_SERVICE_QUEUE} queue")

        channel.close()
    except Exception as e:
        Logger.error(f"Error while publishing message {action} to {settings.USERS_SERVICE_QUEUE} queue")
        raise e
