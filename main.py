from requests import get
import json
import stun
import threading
import server
from client import ChatClient

# For symmetric NAT
client_only_mode = False


# Get network information (NAT type, external IP, external port)
def get_network_info():
    nat_type, external_ip, external_port = stun.get_ip_info()
    return nat_type, external_ip, external_port


# Initialize the chat client
chat_client = ChatClient()

# Read connections.json
with open("./data/connections.json") as f:
    connections = json.load(f)

# Check if connections.json is empty
if not connections:
    # Get IP address
    try:
        ip = get("https://api6.ipify.org").text
        # Start the server
        server_port = server.start_ipv6_server(ip)
        # Update connections.json with our information
        connections[ip] = server_port
        with open("./data/connections.json", "w") as f:
            json.dump(connections, f)
    except Exception:
        nat_type, external_ip, external_port = get_network_info()
        if nat_type == "Symmetric NAT":
            client_only_mode = True
else:
    # Connect to existing peers
    for peer_ip, peer_port in connections.items():
        chat_client.connect_to_peer(peer_ip, peer_port)

# Start the chat
chat_client.start_chat()
