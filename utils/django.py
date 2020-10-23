import os


# TODO: A better way for getting the django host
def get_host():
    """Returns Django host"""

    host = os.environ.get("ALLOWED_HOSTS").split(" ")
    return host


def get_port():
    """Returns Django port"""
    django_port = os.os.environ.get("DJANGO_PORT")
    return django_port
