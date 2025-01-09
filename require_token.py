import os
from functools import wraps

from flask import request


def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        token = request.args.get("hub.verify_token")

        if not token:
            return "Verify Token Required", 401

        if token != os.getenv("VERIFY_TOKEN"):
            return "Incorrect verify token", 401

        return f("", *args, **kwargs)

    return decorated
