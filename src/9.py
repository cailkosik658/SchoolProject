import random
def get_random_number(n):
    if n == 1:
        return random.randint(0, 9)
    else:
        return random.choice([i for i in range(10) if i != get_random_number(n-1)])