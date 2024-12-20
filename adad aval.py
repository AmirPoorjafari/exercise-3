


def sieve_of_eratosthenes(limit):
   
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  
 
    
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
   
   
    return [i for i in range(limit + 1) if primes[i]]

limit = 10_000_000
prime_numbers = sieve_of_eratosthenes(limit)

print(f' {len(prime_numbers)}')
print(f' {prime_numbers[:10]}')  
