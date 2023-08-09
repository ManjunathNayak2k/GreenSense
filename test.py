
def create_large_list():
    large_list = list(range(1000000))
    return large_list

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def give_output(n):
    if n <= 1:
        return n
    else:
        return give_output(n-1) + give_output(n-2)
