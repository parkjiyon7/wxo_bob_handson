"""
User Model
Represents a user in the system with basic information
"""

from datetime import datetime
from typing import Optional


class User:
    """User model with basic attributes"""
    
    def __init__(self, username: str, name: str, age: int, user_id: Optional[int] = None):
        self.id = user_id
        self.username = username
        self.name = name
        self.age = age
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def getUserData(self) -> dict:
        """
        Get user data as dictionary
        TODO: This function name should follow Python naming conventions (snake_case)
        """
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'age': self.age,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def update_name(self, new_name: str) -> None:
        """Update user's name"""
        self.name = new_name
        self.updated_at = datetime.now()
    
    def update_age(self, new_age: int) -> None:
        """
        Update user's age
        TODO: Add age validation (should be positive and reasonable)
        """
        self.age = new_age
        self.updated_at = datetime.now()
    
    def is_adult(self) -> bool:
        """Check if user is an adult (18 or older)"""
        return self.age >= 18
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, username='{self.username}', name='{self.name}')"
    
    def __str__(self) -> str:
        return f"{self.name} (@{self.username})"

# Made with Bob
