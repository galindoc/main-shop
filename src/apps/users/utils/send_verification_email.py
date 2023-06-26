from django.conf import settings

from src.aws import VERIFY_ACCOUNT_QUEUE_URL, enqueue
from src.logger import Logger


def send_verification_email(user):
    try:
        action_url = f'{settings.SERVICE_URL}/{settings.ENDPOINT_PREFIX}/verify-account/{user.verification_token}/'
        enqueue(
            VERIFY_ACCOUNT_QUEUE_URL,
            {
                'receiver_email': user.email,
                'email_type': 'VERIFY_ACCOUNT',
                'action_url': action_url,
                'replacements': {
                    'user_name': user.name,
                },
            },
        )
        Logger.info(f"Sent verification email to {user.email}")
    except Exception as e:
        Logger.error(e)
