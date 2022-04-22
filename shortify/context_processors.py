import socket
from django.utils import timezone


def get_hostname(request):
    return {
        "hostname": socket.gethostname(),
    }


def get_current_year(request):
    now = timezone.now()
    return {
        "current_year": now.year
    }
