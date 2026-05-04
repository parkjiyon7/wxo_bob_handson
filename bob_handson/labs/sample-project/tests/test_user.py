"""
Tests for User model and UserController
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.models.user import User
from src.controllers.user_controller import UserController


class TestUser:
    """Test cases for User model"""
    
    def test_create_user(self):
        """Test user creation"""
        user = User(username="john_doe", name="John Doe", age=25)
        assert user.username == "john_doe"
        assert user.name == "John Doe"
        assert user.age == 25
    
    def test_get_user_data(self):
        """Test getUserData method"""
        user = User(username="jane_doe", name="Jane Doe", age=30, user_id=1)
        data = user.getUserData()
        
        assert data['id'] == 1
        assert data['username'] == "jane_doe"
        assert data['name'] == "Jane Doe"
        assert data['age'] == 30
    
    def test_is_adult(self):
        """Test is_adult method"""
        adult = User(username="adult", name="Adult User", age=20)
        minor = User(username="minor", name="Minor User", age=15)
        
        assert adult.is_adult() is True
        assert minor.is_adult() is False
    
    def test_update_name(self):
        """Test name update"""
        user = User(username="test", name="Old Name", age=25)
        user.update_name("New Name")
        assert user.name == "New Name"


class TestUserController:
    """Test cases for UserController"""
    
    def test_create_user(self):
        """Test creating a user through controller"""
        controller = UserController()
        user = controller.create_user("test_user", "Test User", 25)
        
        assert user.username == "test_user"
        assert user.id == 1
        assert len(controller.users) == 1
    
    def test_get_user_by_id(self):
        """Test getting user by ID"""
        controller = UserController()
        user = controller.create_user("test", "Test", 25)
        
        found = controller.get_user_by_id(user.id)
        assert found is not None
        assert found.username == "test"
    
    def test_get_user_by_username(self):
        """Test getting user by username"""
        controller = UserController()
        controller.create_user("john", "John", 25)
        
        found = controller.get_user_by_username("john")
        assert found is not None
        assert found.name == "John"
    
    def test_update_user(self):
        """Test updating user"""
        controller = UserController()
        user = controller.create_user("test", "Old Name", 25)
        
        updated = controller.update_user(user.id, name="New Name", age=30)
        assert updated.name == "New Name"
        assert updated.age == 30
    
    def test_update_user_with_negative_age(self):
        """
        Test updating user with negative age
        BUG: This test should fail because controller doesn't validate age!
        """
        controller = UserController()
        user = controller.create_user("test", "Test", 25)
        
        # This should raise an error but doesn't!
        updated = controller.update_user(user.id, age=-5)
        # BUG: Negative age is accepted
        assert updated.age == -5  # This passes but shouldn't!
    
    def test_delete_user(self):
        """Test deleting user"""
        controller = UserController()
        user = controller.create_user("test", "Test", 25)
        
        result = controller.delete_user(user.id)
        assert result is True
        assert len(controller.users) == 0
    
    def test_get_adult_users(self):
        """Test getting adult users"""
        controller = UserController()
        controller.create_user("adult1", "Adult 1", 20)
        controller.create_user("minor1", "Minor 1", 15)
        controller.create_user("adult2", "Adult 2", 25)
        
        adults = controller.get_adult_users()
        assert len(adults) == 2

# Made with Bob
