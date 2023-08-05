
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@lru_cache(maxsize=None)
def give_output(n):
    if n <= 1:
        return n
    else:
        return give_output(n-1) + give_output(n-2)

def create_large_list():
    return list(range(1000000))
