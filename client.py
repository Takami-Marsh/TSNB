import socket
import threading
import json

class ChatClient:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.connected_peers = {}
        self.username = input("Enter your username: ")

    def connect_to_peer(self, peer_ip, peer_port):
        try:
            self.socket.connect((peer_ip, peer_port))
            print(f"Connected to peer at {peer_ip}:{peer_port}")
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
            return True
        except Exception as e:
            print(f"Failed to connect to peer: {e}")
            return False

    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}")
            except:
                print("Lost connection to peer")
                break

    def send_message(self, message):
        try:
            full_message = f"{self.username}: {message}"
            self.socket.send(full_message.encode('utf-8'))
        except Exception as e:
            print(f"Failed to send message: {e}")

    def start_chat(self):
        while True:
            message = input("")
            if message.lower() == 'quit':
                break
            self.send_message(message)

        self.socket.close()