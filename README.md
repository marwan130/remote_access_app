# Remote Access Application

A secure remote access and control application that allows one computer to remotely access and control another computer, similar to TeamViewer.

## Features

- Secure authentication using IP address and password
- Remote desktop viewing and control
- File transfer capabilities
- Chat functionality
- Session recording
- Encrypted communication

## Team Division

### Member 1: Networking Infrastructure and Authentication
**Main Focus**: Core socket communication, secure transmission (SSL), and connection handling.

**Assigned Files**:
- `core/socket_utils.py` - Send/recv wrapper functions
- `core/config.py` - PORT, BUFFER_SIZE, IPs
- `core/message_parser.py` - Structuring messages (chat, file, etc.)
- `server/auth.py` - IP + password validation logic
- `tests/test_connection.py` - Connection and handshake tests

**Responsibilities**:
- Build reusable networking interface (send, receive, error handling)
- Add SSL for secure communication
- Handle client authentication via IP/password
- Centralize config constants

### Member 2: File Transfer System
**Main Focus**: Upload and download of files between client and host, with progress/status.

**Assigned Files**:
- `client/file_client.py` - Select and send files
- `server/file_server.py` - Receive and save files
- `shared/logger.py` - Log file transfers
- `tests/test_file_transfer.py` - File transfer success tests

**Responsibilities**:
- Chunk file sending logic (send_file, receive_file)
- Add file size metadata for progress tracking
- Validate file types/extensions if needed
- Log transfers with timestamp and size

### Member 3: Chat + Session Recording
**Main Focus**: Real-time text chat + screen recording on the host during session.

**Assigned Files**:
- `client/chat_client.py` - Text input/output handling
- `server/chat_server.py` - Broadcast or receive chat
- `server/recorder_server.py` - Host-side screen capture + record
- `client/recorder_client.py` - View/receive recorded video (optional)
- `tests/test_chat.py` - Basic chat tests

**Responsibilities**:
- Define chat message protocol (type: chat, content, timestamp)
- Use threading for real-time bidirectional chat
- Use mss + OpenCV to record screen to .mp4
- Optionally allow video file playback on client side

### Member 4: GUI (Tkinter) + App Launch
**Main Focus**: Design and build GUI with Tkinter, wire it to backend features.

**Assigned Files**:
- `client/gui.py` - Chat box, file upload, connect form
- `client/main.py` - Entry point for client-side app
- `server/main.py` - Entry point for server-side app
- `README.md` - Usage instructions for GUI

**Responsibilities**:
- Create a Tkinter GUI with:
  - IP input + Connect button
  - Chat view + input
  - File chooser + send button
- Call the appropriate backend methods (file, chat, etc.) from GUI
- Handle GUI responsiveness using threading

### Summary Table

| Member | Role | Functionalities | Key Files |
|--------|------|----------------|-----------|
| 1 | Sockets & Auth | TCP/SSL, connection, config, IP/password auth | socket_utils.py, auth.py, config.py |
| 2 | File Transfer | File sending/receiving, progress, logging | file_client.py, file_server.py, logger.py |
| 3 | Chat + Screen Recording | Real-time messaging + session video recording | chat_client.py, chat_server.py, recorder_server.py |
| 4 | GUI + Integration | Build interface + integrate chat/file/auth | gui.py, main.py |

## Setup

1. Create and activate a virtual environment:
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get a security error, you might need to run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

## Running the Application

### Server (Host Machine)
```powershell
python .\server\main.py
```

### Client
```powershell
python .\client\main.py
```

## Security Features

- SSL/TLS encryption for all communications
- IP-based access control
- Password authentication
- Session logging

## Testing

Run tests using pytest:
```powershell
pytest .\tests\
```

## Troubleshooting

### Common Issues

1. PowerShell Execution Policy
```powershell
# If you can't activate the virtual environment, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. Port Access
```powershell
# If you get port access errors, run PowerShell as Administrator
Start-Process powershell -Verb RunAs
```

3. SSL Certificate
- Make sure `server.crt` and `server.key` are in the root directory
- For development, self-signed certificates will be automatically generated

### Environment Variables

Create a `.env` file in the root directory with:
```
PASSWORD_SALT=your_secure_salt_here
```