import socket
from django.utils import timezone


def get_hostname(request):
    return {
        "hostname": socket.gethostname(),
    }
