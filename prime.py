## Inspiration. I was in this random class where we were learning about prime numbers, especially Euclid's theory of prime numbers

# So I thought two things
# 1. Is there any interesting pattern between the difference between prime numbers?
# 2. And then, assuming we go to infinity, what is the longest difference between prime numbers?

# That is what I want to figure out. 

import matplotlib.pyplot as plt
import math
import numpy as np
import scipy


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


primes = generate_primes(20000)
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

# Largest difference
print(f"The two prime numbers with this difference are {prime1} and {prime2}")

# Second largest difference TBD
print(f"The")

print(diffs)


# Plot
plt.plot(diffs)
plt.title("Differences Between Consecutive Prime Numbers")
plt.xlabel("Number of Primes")
plt.ylabel("Difference")
plt.show()





## What happens if you take the fourier transform of the differences between consecutive prime numbers? 
## Maybe in the fourier transform, we can see some interesting patterns such as different frequencies.

## Let's try it out

# Fourier Transform


# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(1, len(diffs), len(diffs))
y = diffs
yf = scipy.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# print("x axis", x)

# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

# plt.grid()

# plt.show()




# Why the fourier transform? It's what frequency fits your data. If it's a sine wave, it would be a perfect spike. If there's only one frequency, if it's 
# the frequency that is most common is whatever that spike is. The most common difference.