# TSNB - Peer-to-Peer Chat Application

TSNB is a decentralized peer-to-peer chat application that enables direct communication between users without relying on a central server. It supports IPv6 connectivity and handles various NAT configurations.

## Dependencies

- External packages:
  - `requests`: For IP address discovery
  - `pystun3`: For NAT type detection and traversal

## Installation

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install requests pystun3
   ```

## Usage

1. Start the application:

   ```bash
   python main.py
   ```

2. When first starting, you'll be prompted to enter a username.

3. The application will automatically:

   - Detect your network configuration
   - Set up as a server if you're the first peer
   - Connect to existing peers if others are already in the network

4. Start chatting! Type your messages and press Enter to send.

5. To exit the chat, type 'quit' and press Enter.

## Technical Details

### Network Architecture

- Uses IPv6 for peer connectivity
- Implements STUN protocol for NAT traversal
- Supports peer discovery through shared connection information
- Handles various NAT types including symmetric NAT

### Features

- Real-time messaging between peers
- Username-based message identification
- Automatic peer discovery and connection
- Graceful connection handling and error recovery

### File Structure

- `main.py`: Application entry point and network initialization
- `client.py`: Chat client implementation
- `server.py`: Server functionality for peer connections
- `data/connections.json`: Peer connection information storage
