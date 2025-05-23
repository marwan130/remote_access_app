from core.socket_utils import SecureSocket
from core.message_parser import MessageParser, MessageType
from core.config import CHUNK_SIZE, MAX_FILE_SIZE

class FileTransferClient:
    def __init__(self, host: str, port: int):
        """Initialize the file transfer client."""
        pass

    def send_file(self, filepath: str):
        """Send a file to the server."""
        pass

    def receive_file(self, filename: str):
        """Receive a file from the server."""
        pass 