import logging
import os
from base64 import b64decode, b64encode
from hashlib import sha256
from random import randrange

SECRET = os.urandom(randrange(10, 20))

logger = logging.getLogger("app")


def hash_password(password) -> str:
    """ Hash password with a known secure hashing function """
    return sha256(password.encode()).hexdigest()


def sign(message: str) -> bytes:
    """Sign message with a super secret key"""
    return sha256(SECRET + message).digest()


def verify(data: bytes, sig: bytes) -> bool:
    """ Verify supplied signature. Return boolean based on result"""
    return sign(data) == sig


def parse_session(cookie: bytes) -> dict:
    """ Parse cookie and return dict
        @cookie: "key1=value1;key2=value2"

        return {"key1":"value1","key2":"value2"}
    """
    parsed = {}
    b64_data, b64_sig = cookie.split('.')
    data = b64decode(b64_data)
    sig = b64decode(b64_sig)
    if not verify(data, sig):
        raise ValueError
    for group in data.split(b';'):
        try:
            if not group:
                continue
            key, val = group.split(b'=')
            parsed[key.decode()] = val
        except Exception:
            continue
    return parsed


def create_session(user_data: dict) -> bytes:
    """ Create session based on dict
    param data: {"username": username, "secret": password}
    return: key value pairs in "key1=value1;key2=value2;"
    """
    session = ""
    for k, v in user_data.items():
        session += f"{k}={v};"
    return session.encode()


def get_session(request) -> dict:
    """ Get user specific session and verify signature """
    if not request.cookies or "auth" not in request.cookies:
        return
    cookie = request.cookies.get("auth")
    try:
        user_data = parse_session(cookie)
    except ValueError:
        logger.warning("Invalid signature detected! Session will get killed.")
        return {"message": "Invalid signature", "error": 403}
    return user_data


def create_cookie(session):
    """Create cookie for continuous authentication"""
    cookie_sig = sign(session)
    return b64encode(session) + b'.' + b64encode(cookie_sig)
