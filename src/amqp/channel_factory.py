import pika
from django.conf import settings


def channel_factory():
    try:
        connection = pika.BlockingConnection(pika.URLParameters(
            'amqps://{username}:{password}@{host}'.format(
                username=settings.RABBITMQ_DEFAULT_USER,
                password=settings.RABBITMQ_DEFAULT_PASS,
                host=settings.RABBITMQ_HOST,
            )
        ))
        return connection.channel()
    except Exception as e:
        raise e
