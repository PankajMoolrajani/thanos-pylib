"""
Thanos PyLib - A Hello World Python Library
"""

__version__ = "0.1.0"


def hello_world():
    """
    Returns a hello world message.
    
    Returns:
        str: A hello world message
    """
    return "Hello, World from Thanos PyLib!"


def greet(name):
    """
    Returns a personalized greeting.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A personalized greeting message
    """
    return f"Hello, {name}! Welcome to Thanos PyLib!"
