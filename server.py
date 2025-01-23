import socket
import threading

server_socket = None
connected_clients = {}

def receive():
    global server_socket, connected_clients
    server_socket.listen(5)
    while True:
        client, address = server_socket.accept()
        print(f"Connection from {address}")
        connected_clients[address] = client
        client_thread = threading.Thread(target=handle_client, args=(client, address))
        client_thread.start()

def handle_client(client, address):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast(message, address)
        except:
            break
    remove_client(address)

def broadcast(message, sender_address):
    for addr, client in connected_clients.items():
        if addr != sender_address:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(addr)

def remove_client(address):
    if address in connected_clients:
        connected_clients[address].close()
        del connected_clients[address]

def start_ipv6_server(ipv6_address):
    global server_socket
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # Loop until an open port is found
    port = 27463
    while True:
        try:
            server_socket.bind((ipv6_address, port))
            break
        except Exception:
            port += 1
            pass
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    return port
