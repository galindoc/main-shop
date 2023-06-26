import json
import os

import boto3


# Credentials
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Queues
VERIFY_ACCOUNT_QUEUE_URL = 'VERIFY_ACCOUNT_QUEUE_URL'


def enqueue(queue_url, message_body):
    client = boto3.client(
        'sqs',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME,
    )
    queue_url = os.getenv(queue_url)

    return client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message_body),   
    )
