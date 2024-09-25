import socket
import threading
import json

def handle_client_connection(client_socket, port):
    try:
        print(f"[INFO] Connection received on port {port}")
        
        # Receive the data in chunks
        data = b""
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            data += chunk
        
        # Decode and parse the JSON data
        try:
            json_data = json.loads(data.decode())
            print(f"[INFO] Received JSON data from port {port}: {json_data}")
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to decode JSON data: {e}")
        
        client_socket.close()
    except Exception as e:
        print(f"[ERROR] {e}")

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[INFO] Listening on 0.0.0.0:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[INFO] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket, port))
        client_handler.start()