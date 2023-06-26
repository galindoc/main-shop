from secrets import token_urlsafe

from slugify import slugify


def create_verification_token():
    return slugify(token_urlsafe(16))
