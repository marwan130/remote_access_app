import hashlib
import os
from typing import Tuple
from shared.logger import RemoteAccessLogger
from core.config import PASSWORD_SALT

class Authenticator:
    def __init__(self):
        self.logger = RemoteAccessLogger("authenticator")
        self.allowed_ips = set()
        self.authenticated_clients = set()
        
    def hash_password(self, password: str) -> str:
        """Hash the password with salt using SHA-256."""
        salted = password + PASSWORD_SALT
        return hashlib.sha256(salted.encode()).hexdigest()
    
    def authenticate(self, client_ip: str, password: str) -> Tuple[bool, str]:
        """
        Authenticate a client based on IP and password.
        Returns (success, message).
        """
        # Check if client is already authenticated
        if client_ip in self.authenticated_clients:
            return True, "Already authenticated"
            
        # Hash the provided password
        hashed_password = self.hash_password(password)
        
        # In a real application, you would compare with a stored password
        # For demo purposes, we'll use a hardcoded password
        DEMO_PASSWORD_HASH = self.hash_password("demo123")
        
        if hashed_password == DEMO_PASSWORD_HASH:
            self.authenticated_clients.add(client_ip)
            self.allowed_ips.add(client_ip)
            self.logger.log_auth(client_ip, True)
            return True, "Authentication successful"
        
        self.logger.log_auth(client_ip, False)
        return False, "Invalid password"
    
    def is_authenticated(self, client_ip: str) -> bool:
        """Check if a client IP is authenticated."""
        return client_ip in self.authenticated_clients
    
    def revoke_authentication(self, client_ip: str) -> None:
        """Revoke authentication for a client."""
        if client_ip in self.authenticated_clients:
            self.authenticated_clients.remove(client_ip)
            self.allowed_ips.remove(client_ip)
            self.logger.log_security_event(
                "auth_revoked",
                f"Authentication revoked for client {client_ip}"
            )
            
    def add_allowed_ip(self, ip: str) -> None:
        """Add an IP to the allowed list."""
        self.allowed_ips.add(ip)
        self.logger.log_security_event(
            "ip_allowed",
            f"IP {ip} added to allowed list"
        )
        
    def remove_allowed_ip(self, ip: str) -> None:
        """Remove an IP from the allowed list."""
        if ip in self.allowed_ips:
            self.allowed_ips.remove(ip)
            self.revoke_authentication(ip)
            self.logger.log_security_event(
                "ip_blocked",
                f"IP {ip} removed from allowed list"
            ) 