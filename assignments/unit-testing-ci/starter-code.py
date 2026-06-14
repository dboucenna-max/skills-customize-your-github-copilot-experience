"""Simple utility functions for students to test."""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Divide `a` by `b`. Raise ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def is_even(n):
    """Return True if `n` is even, False otherwise."""
    return n % 2 == 0
