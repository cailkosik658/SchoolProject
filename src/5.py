
import random

def get_random_code(length=10):
    # Generate a random string of letters and digits
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    code = ''
    for i in range(length):
        code += random.choice(letters + digits)
    return code