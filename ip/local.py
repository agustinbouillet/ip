import socket


def local():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)
