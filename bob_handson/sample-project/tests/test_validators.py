"""
Tests for validation utilities
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.validators import (
    validate_username, 
    validate_age, 
    validate_email,
    validate_password
)


class TestValidators:
    """Test cases for validation functions"""
    
    def test_validate_username_valid(self):
        """Test valid usernames"""
        valid, msg = validate_username("john_doe")
        assert valid is True
        
        valid, msg = validate_username("user123")
        assert valid is True
    
    def test_validate_username_too_short(self):
        """Test username too short"""
        valid, msg = validate_username("ab")
        assert valid is False
        assert "at least 3" in msg
    
    def test_validate_username_too_long(self):
        """Test username too long"""
        valid, msg = validate_username("a" * 21)
        assert valid is False
        assert "at most 20" in msg
    
    def test_validate_username_invalid_chars(self):
        """Test username with invalid characters"""
        valid, msg = validate_username("user@name")
        assert valid is False
        assert "letters, numbers, and underscores" in msg
    
    def test_validate_age_valid(self):
        """Test valid ages"""
        valid, msg = validate_age(25)
        assert valid is True
        
        valid, msg = validate_age(0)
        assert valid is True
    
    def test_validate_age_negative(self):
        """Test negative age"""
        valid, msg = validate_age(-5)
        assert valid is False
        assert "negative" in msg
    
    def test_validate_age_unrealistic(self):
        """Test unrealistic age"""
        valid, msg = validate_age(200)
        assert valid is False
        assert "unrealistic" in msg
    
    def test_validate_email_valid(self):
        """Test valid email"""
        valid, msg = validate_email("user@example.com")
        assert valid is True
        
        valid, msg = validate_email("test.user@domain.co.uk")
        assert valid is True
    
    def test_validate_email_invalid(self):
        """Test invalid email"""
        valid, msg = validate_email("notanemail")
        assert valid is False
        
        valid, msg = validate_email("@example.com")
        assert valid is False
        
        valid, msg = validate_email("user@")
        assert valid is False
    
    def test_validate_password_valid(self):
        """Test valid password"""
        valid, msg = validate_password("password123")
        assert valid is True
    
    def test_validate_password_too_short(self):
        """Test password too short"""
        valid, msg = validate_password("pass")
        assert valid is False
        assert "at least 8" in msg

# Made with Bob
