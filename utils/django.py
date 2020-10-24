import os


# TODO: A better way for getting the django host
def get_host():
    """Returns a Django host"""

    all_hosts = os.environ.get("ALLOWED_HOSTS").split(" ")
    host = all_hosts[0]
    return host


def get_port():
    """Returns Django port"""
    django_port = os.environ.get("DJANGO_PORT")
    return django_port
