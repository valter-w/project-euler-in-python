def get_prime(index):
    if index < 1: return None

    primes = []
    n = 2
    while len(primes) < index:
        for prime in primes:
            if n % prime == 0:
                break
        else:
            primes.append(n)

        n += 1
            
    return primes[-1]

print(get_prime(10_001))