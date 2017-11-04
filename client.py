import socket
import time
from server import port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', port))
client_socket.settimeout(5)

time.sleep(5)
client_socket.sendall("Hello there!\r\n")

time.sleep(5)
client_socket.close()
