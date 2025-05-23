import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Network Configuration
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000
CHAT_PORT = 5001
FILE_TRANSFER_PORT = 5002
SCREEN_SHARE_PORT = 5003

# Buffer Sizes
BUFFER_SIZE = 4096
SCREEN_BUFFER_SIZE = 65536
FILE_BUFFER_SIZE = 8192

# Security
SSL_CERT_FILE = "server.crt"
SSL_KEY_FILE = "server.key"
PASSWORD_SALT = os.getenv("PASSWORD_SALT", "default_salt")

# Screen Recording
FRAME_RATE = 30
SCREEN_QUALITY = 80  # JPEG compression quality (1-100)

# File Transfer
MAX_FILE_SIZE = 1024 * 1024 * 1024  # 1GB
CHUNK_SIZE = 8192

# Logging
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "remote_access.log"

# GUI Configuration
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
CHAT_WIDTH = 300
TOOLBAR_HEIGHT = 40 