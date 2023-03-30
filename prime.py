## Write code to record the difference between primes and also record the longest difference you can find between prime numbers. 

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = math.floor(math.sqrt(n))
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i += 2
    return True
