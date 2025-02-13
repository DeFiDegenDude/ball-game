import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Function to send messages to the server
def send_messages():
    while True:
        message = input("")
        client.send(message.encode('utf-8'))

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
