from enum import Enum
from typing import Dict, Any, Optional
import json
import base64

class MessageType(Enum):
    AUTH = "auth"
    CHAT = "chat"
    FILE_START = "file_start"
    FILE_CHUNK = "file_chunk"
    FILE_END = "file_end"
    SCREEN_DATA = "screen_data"
    MOUSE_EVENT = "mouse_event"
    KEYBOARD_EVENT = "keyboard_event"
    ERROR = "error"
    DISCONNECT = "disconnect"

class MessageParser:
    @staticmethod
    def create_message(msg_type: MessageType, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a formatted message with type and data."""
        return {
            "type": msg_type.value,
            "data": data
        }

    @staticmethod
    def parse_message(message: Dict[str, Any]) -> Optional[tuple[MessageType, Dict[str, Any]]]:
        """Parse a received message and return its type and data."""
        try:
            msg_type = MessageType(message["type"])
            return msg_type, message["data"]
        except (KeyError, ValueError):
            return None

    @staticmethod
    def create_auth_message(password: str, client_ip: str) -> Dict[str, Any]:
        """Create an authentication message."""
        return MessageParser.create_message(
            MessageType.AUTH,
            {
                "password": password,
                "client_ip": client_ip
            }
        )

    @staticmethod
    def create_chat_message(sender: str, content: str) -> Dict[str, Any]:
        """Create a chat message."""
        return MessageParser.create_message(
            MessageType.CHAT,
            {
                "sender": sender,
                "content": content,
                "timestamp": import_time()
            }
        )

    @staticmethod
    def create_file_start_message(filename: str, file_size: int) -> Dict[str, Any]:
        """Create a file transfer start message."""
        return MessageParser.create_message(
            MessageType.FILE_START,
            {
                "filename": filename,
                "size": file_size
            }
        )

    @staticmethod
    def create_file_chunk_message(chunk: bytes) -> Dict[str, Any]:
        """Create a file chunk message."""
        return MessageParser.create_message(
            MessageType.FILE_CHUNK,
            {
                "data": base64.b64encode(chunk).decode()
            }
        )

    @staticmethod
    def create_screen_data_message(image_data: bytes) -> Dict[str, Any]:
        """Create a screen data message."""
        return MessageParser.create_message(
            MessageType.SCREEN_DATA,
            {
                "image": base64.b64encode(image_data).decode()
            }
        )

    @staticmethod
    def create_mouse_event_message(x: int, y: int, event_type: str) -> Dict[str, Any]:
        """Create a mouse event message."""
        return MessageParser.create_message(
            MessageType.MOUSE_EVENT,
            {
                "x": x,
                "y": y,
                "type": event_type
            }
        )

    @staticmethod
    def create_keyboard_event_message(key: str, event_type: str) -> Dict[str, Any]:
        """Create a keyboard event message."""
        return MessageParser.create_message(
            MessageType.KEYBOARD_EVENT,
            {
                "key": key,
                "type": event_type
            }
        )

    @staticmethod
    def create_error_message(error_code: str, message: str) -> Dict[str, Any]:
        """Create an error message."""
        return MessageParser.create_message(
            MessageType.ERROR,
            {
                "code": error_code,
                "message": message
            }
        ) 