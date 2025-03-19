import random

def get_random_code(length=10):
    """Returns a random string of length `length` consisting only of uppercase letters."""
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))
