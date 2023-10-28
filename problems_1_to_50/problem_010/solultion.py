primes = []
sum = 0
for n in range(2, 2_000_000):
    for prime in primes:
        if n % prime == 0:
            break
    else:
         primes.append(n)
         sum += n
            

print(sum)