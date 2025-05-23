import socket
import ssl
from typing import Tuple, Optional
import json

from core.config import (
    SSL_CERT_FILE,
    SSL_KEY_FILE,
    BUFFER_SIZE
)

class SecureSocket:
    def __init__(self, host: str, port: int, is_server: bool = False):
        self.host = host
        self.port = port
        self.is_server = is_server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ssl_context = self._create_ssl_context()
        self.secure_socket = None
        
    def _create_ssl_context(self) -> ssl.SSLContext:
        context = ssl.create_default_context(
            ssl.Purpose.CLIENT_AUTH if self.is_server else ssl.Purpose.SERVER_AUTH
        )
        
        if self.is_server:
            context.load_cert_chain(certfile=SSL_CERT_FILE, keyfile=SSL_KEY_FILE)
        else:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
        return context
    
    def start_server(self) -> None:
        """Start the server socket."""
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        
    def accept(self) -> Tuple[ssl.SSLSocket, Tuple[str, int]]:
        """Accept a client connection."""
        if not self.is_server:
            raise RuntimeError("Cannot accept connections on a client socket")
        
        client_socket, addr = self.socket.accept()
        secure_client = self.ssl_context.wrap_socket(client_socket, server_side=True)
        return secure_client, addr
    
    def connect(self) -> None:
        """Connect to a server."""
        if self.is_server:
            raise RuntimeError("Cannot connect with a server socket")
            
        self.socket.connect((self.host, self.port))
        self.secure_socket = self.ssl_context.wrap_socket(
            self.socket, server_hostname=self.host
        )
        
    def send(self, data: dict) -> None:
        """Send encrypted data."""
        json_data = json.dumps(data)
        encoded_data = json_data.encode()
        if self.secure_socket:
            self.secure_socket.send(encoded_data)
            
    def receive(self) -> Optional[dict]:
        """Receive and decrypt data."""
        if self.secure_socket:
            try:
                data = self.secure_socket.recv(BUFFER_SIZE)
                if not data:
                    return None
                decoded_data = data.decode()
                return json.loads(decoded_data)
            except (json.JSONDecodeError, UnicodeDecodeError):
                return None
            
    def close(self) -> None:
        """Close the socket connection."""
        if self.secure_socket:
            self.secure_socket.close()
        self.socket.close() 