"""
User Controller
Handles user-related operations and business logic
"""

from typing import List, Optional
from ..models.user import User
from ..utils.validators import validate_username, validate_age


class UserController:
    """Controller for managing user operations"""
    
    def __init__(self):
        self.users: List[User] = []
        self._next_id = 1
    
    def create_user(self, username: str, name: str, age: int) -> User:
        """
        Create a new user
        TODO: Add input validation before creating user
        TODO: Check for duplicate usernames
        """
        # Basic validation (intentionally incomplete for demo)
        if not username:
            raise ValueError("Username cannot be empty")
        
        user = User(username=username, name=name, age=age, user_id=self._next_id)
        self.users.append(user)
        self._next_id += 1
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def get_all_users(self) -> List[User]:
        """Get all users"""
        return self.users.copy()
    
    def update_user(self, user_id: int, name: Optional[str] = None, 
                   age: Optional[int] = None) -> Optional[User]:
        """
        Update user information
        BUG: This function doesn't validate age before updating
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        if name:
            user.update_name(name)
        if age is not None:
            # BUG: Missing age validation - negative ages are allowed!
            user.update_age(age)
        
        return user
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID"""
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
    
    def get_adult_users(self) -> List[User]:
        """Get all adult users (18+)"""
        return [user for user in self.users if user.is_adult()]
    
    def get_users_data(self) -> List[dict]:
        """
        Get all users data as list of dictionaries
        Uses getUserData() method from User model
        """
        return [user.getUserData() for user in self.users]

# Made with Bob
