import socket

name = socket.gethostname()

ip = socket.gethostbyname(name)

more = socket.gethostbyaddr(ip)

print(ip)
print(more)
