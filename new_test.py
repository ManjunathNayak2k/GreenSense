
def multiply_matrices(a, b):
    rowA, colA = len(a), len(a[0])
    rowB, colB = len(b), len(b[0])
    
    if colA != rowB:
        print("Incompatible matrices.")
        return

    result = [[0 for _ in range(colB)] for _ in range(rowA)]

    for i in range(rowA):
        for j in range(colB):
            for k in range(colA): # or, we could use rowB
                result[i][j] += a[i][k] * b[k][j]
    return result

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def print_primes_up_to_n(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i)

import random

def estimate_pi(n):
    num_points_in_circle = 0
    num_total_points = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_in_circle += 1
        num_total_points += 1

    return 4 * num_points_in_circle / num_total_points
