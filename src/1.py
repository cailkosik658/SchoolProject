def get_random_python_code():
    return """import random

def get_random_number(n):
    return random.randint(0, n)

if __name__ == "__main__":
    print(get_random_number(10))"""
