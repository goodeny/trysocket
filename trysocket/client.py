import socket
import sys

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 9999)
        self.client_socket.connect(self.server_address)

    def set_user(self, user):
        self.client_socket.send(user)

    def send_message(self, message):
        self.client_socket.send(message)