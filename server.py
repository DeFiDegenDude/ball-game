import socket
import threading

# Function to handle client communication
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client says: {message}")
                # Broadcasting message to all clients
                broadcast(message, client_socket)
            else:
                break
        except:
            break
    client_socket.close()

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                continue

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5))
server.listen(5)
print("Server started. Waiting for connections...")

clients = []

# Accepting multiple clients and starting new threads for each
while True:
    client_socket, client_address = server.accept()
    print(f"Connection established with {client_address}")
    clients.append(client_socket)
    
    # Start a new thread for handling client communication
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
