"""
Analytics utilities for user statistics
This module needs refactoring for better readability and performance
"""

from typing import List, Dict, Any


def calculate_statistics(users: List[Any]) -> Dict[str, Any]:
    """
    Calculate statistics from user list
    TODO: This function is too complex and hard to read - needs refactoring
    PERFORMANCE: This could be optimized with better algorithms
    """
    if not users:
        return {
            'total': 0,
            'average_age': 0,
            'adults': 0,
            'minors': 0
        }
    
    # Calculate total
    total = len(users)
    
    # Calculate ages - inefficient loop
    total_age = 0
    for user in users:
        total_age = total_age + user.age
    
    # Calculate average
    avg_age = total_age / total
    
    # Count adults and minors - another loop (inefficient!)
    adults = 0
    minors = 0
    for user in users:
        if user.age >= 18:
            adults = adults + 1
        else:
            minors = minors + 1
    
    # Return results
    result = {
        'total': total,
        'average_age': avg_age,
        'adults': adults,
        'minors': minors
    }
    
    return result


def generate_report(users: List[Any]) -> str:
    """
    Generate a text report of user statistics
    TODO: Add more detailed statistics
    TODO: Format output better
    """
    stats = calculate_statistics(users)
    
    report = f"""
User Statistics Report
======================
Total Users: {stats['total']}
Average Age: {stats['average_age']:.1f}
Adults (18+): {stats['adults']}
Minors (<18): {stats['minors']}
"""
    
    return report


def find_oldest_user(users: List[Any]) -> Any:
    """
    Find the oldest user
    BUG: Returns None if list is empty, should raise exception
    """
    if not users:
        return None
    
    oldest = users[0]
    for user in users:
        if user.age > oldest.age:
            oldest = user
    
    return oldest


def find_youngest_user(users: List[Any]) -> Any:
    """Find the youngest user"""
    if not users:
        return None
    
    youngest = users[0]
    for user in users:
        if user.age < youngest.age:
            youngest = user
    
    return youngest


def calcualte_total(items: List[float]) -> float:
    """
    Calculate total of items
    TYPO: Function name has a typo - should be 'calculate_total'
    This is intentionally left for Lab 1 Exercise 3
    """
    total = 0
    for item in items:
        total += item
    return total

# Made with Bob
