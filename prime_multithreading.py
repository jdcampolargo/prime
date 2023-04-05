import threading
import matplotlib.pyplot as plt

def is_prime(n):
    """Return True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    """Generate prime numbers between start and end."""
    primes = []
    for i in range(start, end):
        if is_prime(i):
            primes.append(i)
    return primes

def generate_all_primes(n, num_threads):
    """Generate all prime numbers between 2 and n using num_threads threads."""
    primes = []
    threads = []
    chunk_size = n // num_threads
    for i in range(num_threads):
        start = 2 + i * chunk_size
        end = start + chunk_size
        if i == num_threads - 1:
            end = n + 1
        t = threading.Thread(target=lambda p, s, e: p.extend(generate_primes(s, e)), args=(primes, start, end))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    primes.sort()
    return primes

def get_longest_diff(primes):
    """Return the longest difference between consecutive primes and the corresponding prime numbers."""
    diffs = [primes[i] - primes[i-1] for i in range(1, len(primes))]
    longest_diff = max(diffs)
    longest_diff_index = diffs.index(longest_diff)
    prime1 = primes[longest_diff_index]
    prime2 = primes[longest_diff_index + 1]
    return longest_diff, prime1, prime2, diffs

if __name__ == '__main__':
    n = 2000000
    num_threads = 4

    primes = generate_all_primes(n, num_threads)
    longest_diff, prime1, prime2, diffs = get_longest_diff(primes)

    print(f"The longest difference between prime numbers is {longest_diff}")
    print(f"The two prime numbers with this difference are {prime1} and {prime2}")

    # Plot the differences between consecutive primes
    plt.plot(diffs)
    plt.title("Differences Between Consecutive Prime Numbers")
    plt.xlabel("Number of Primes")
    plt.ylabel("Difference")
    plt.show()
