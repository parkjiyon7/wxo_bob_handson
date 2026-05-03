"""
Validation utilities for user input
"""

import re
from typing import Tuple


def validate_username(username: str) -> Tuple[bool, str]:
    """
    Validate username
    Rules: 3-20 characters, alphanumeric and underscore only
    TODO: Add check for reserved usernames (admin, root, etc.)
    """
    if not username:
        return False, "Username cannot be empty"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    
    if len(username) > 20:
        return False, "Username must be at most 20 characters"
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    
    return True, "Valid username"


def validate_age(age: int) -> Tuple[bool, str]:
    """
    Validate age
    TODO: This validation is too simple - needs improvement
    """
    if age < 0:
        return False, "Age cannot be negative"
    
    if age > 150:
        return False, "Age seems unrealistic"
    
    return True, "Valid age"


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validate email address
    SECURITY ISSUE: This regex is too simple and can be bypassed
    TODO: Use a proper email validation library
    """
    if not email:
        return False, "Email cannot be empty"
    
    # Simple regex - NOT production ready!
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Invalid email format"
    
    return True, "Valid email"


def validate_password(password: str) -> Tuple[bool, str]:
    """
    Validate password strength
    TODO: Implement proper password strength checking
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    # TODO: Add checks for uppercase, lowercase, numbers, special characters
    
    return True, "Valid password"

# Made with Bob
