## Inspiration. I was in this random class where we were learning about prime numbers, especially Euclid's theory of prime numbers

# So I thought two things
# 1. Is there any interesting pattern between the difference between prime numbers?
# 2. And then, assuming we go to infinity, what is the longest difference between prime numbers?

# That is what I want to figure out. 

import matplotlib.pyplot as plt
import math
## We need to write a for-loop but we need to get the primes numbers from somewhere so

## generate_primes is function that will generate the prime numbers for us.

# range(2 is the first prime, n`+1 is the last prime number we want to check for prime numbers.)

def generate_primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


primes = generate_primes(2000)
diffs = []
for i in range(1, len(primes)):
    diff = primes[i] - primes[i-1]
    diffs.append(diff)
    # print(f"The difference between {primes[i-1]} and {primes[i]} is {diff}")


longest_diff = max(diffs)
longest_diff_index = diffs.index(longest_diff)

      
prime1 = primes[longest_diff_index]
prime2 = primes[longest_diff_index + 1]


print(f"The longest difference between prime numbers is {longest_diff}")
print(f"The two prime numbers with this difference are {prime1} and {prime2}")


print(diffs)

# Plot
plt.plot(diffs)
plt.title("Differences Between Consecutive Prime Numbers")
plt.xlabel("Index")
plt.ylabel("Difference")
# plt.show()
