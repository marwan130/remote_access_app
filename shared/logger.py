import logging
import os
from datetime import datetime
from typing import Optional
from core.config import LOG_FORMAT, LOG_FILE

class RemoteAccessLogger:
    def __init__(self, name: str, log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create logs directory if it doesn't exist
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Set up file handler
        log_file = log_file or os.path.join(log_dir, LOG_FILE)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        # Set up console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def log_connection(self, client_ip: str, success: bool):
        """Log connection attempts."""
        status = "successful" if success else "failed"
        self.logger.info(f"Connection {status} from {client_ip}")
        
    def log_file_transfer(self, filename: str, size: int, sender: str, receiver: str):
        """Log file transfer events."""
        self.logger.info(
            f"File transfer: {filename} ({size} bytes) from {sender} to {receiver}"
        )
        
    def log_chat_message(self, sender: str, message: str):
        """Log chat messages."""
        self.logger.info(f"Chat message from {sender}: {message}")
        
    def log_error(self, error_message: str, error_type: str = "ERROR"):
        """Log error messages."""
        self.logger.error(f"{error_type}: {error_message}")
        
    def log_auth(self, client_ip: str, success: bool):
        """Log authentication attempts."""
        status = "successful" if success else "failed"
        self.logger.info(f"Authentication {status} for client {client_ip}")
        
    def log_session_start(self, client_ip: str):
        """Log session start."""
        self.logger.info(f"Remote session started with client {client_ip}")
        
    def log_session_end(self, client_ip: str):
        """Log session end."""
        self.logger.info(f"Remote session ended with client {client_ip}")
        
    def log_screen_capture(self, client_ip: str):
        """Log screen capture events."""
        self.logger.debug(f"Screen captured for client {client_ip}")
        
    def log_mouse_event(self, client_ip: str, event_type: str):
        """Log mouse events."""
        self.logger.debug(f"Mouse event {event_type} from client {client_ip}")
        
    def log_keyboard_event(self, client_ip: str, event_type: str):
        """Log keyboard events."""
        self.logger.debug(f"Keyboard event {event_type} from client {client_ip}")
        
    def log_system_info(self, info: dict):
        """Log system information."""
        self.logger.info(f"System info: {info}")
        
    def log_security_event(self, event_type: str, details: str):
        """Log security-related events."""
        self.logger.warning(f"Security event - {event_type}: {details}")
        
    def log_performance_metric(self, metric_name: str, value: float):
        """Log performance metrics."""
        self.logger.info(f"Performance metric - {metric_name}: {value}") 