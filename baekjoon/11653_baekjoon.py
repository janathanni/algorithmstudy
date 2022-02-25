n = int(input())

nums = [0 for _ in range (0, n+1)]

primes = []

for i in range (2, n+1):

    if nums[i] == 0:
        primes.append(i)
        for j in range (i*2, n+1, i):
            nums[j] = 1


while n != 1:
    
    for prime in primes:

        if n%prime == 0:
            print(prime)
            n = n/prime
            break