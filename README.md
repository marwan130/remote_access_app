# Remote Access Application

A secure remote access and control application that allows one computer to remotely access and control another computer, similar to TeamViewer.

## Features

- Secure authentication using IP address and password
- Remote desktop viewing and control
- File transfer capabilities
- Chat functionality
- Session recording
- Encrypted communication

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
