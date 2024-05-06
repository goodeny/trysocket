import socket
import threading
from repository import Database
db = Database()
db.Connect()
# Function to handle incoming client connections
def handle_client(client_socket, client_address):
    #messages = []
    print(f"Accepted connection from {client_address}")
    username = client_socket.recv(1024).decode()
    #print(f"{client_address} set username to: {username}")
    while True:
        # Receive message from client
        data = client_socket.recv(1024)
        if  not data:
            break

        # Broadcast message to all connected clients
        message = data.decode()
        #messages.append([[username], [message]])
        db.setReceive(user=username, message=message)
        broadcast(f"{username}: {message}")

    print(f"Connection from {client_address} closed.")
    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message.encode())

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 9999)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening for connections...")

clients = []

try:
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()

        # Add client to the list of connected clients
        clients.append(client_socket)

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

finally:
    server_socket.close()
