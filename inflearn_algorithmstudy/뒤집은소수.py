def reverse(n, x):
    for i in range(n):
        x[i] == int(x[i][::-1])
    
    return isPrime(x)

def isPrime(x):
    num_lists = [0 for _ in range(0, max(x)+3)]

    for i in range (2, int(max(x)+1)):

        if num_lists[i] == 1:
            continue
        
        else:
            for j in range (i+1, int(max(x)+1)):
                num_lists[j]==1

    prime_lists = []

    for number in x:
        if number in num_lists:
            prime_lists.append(str(number))

    return (' '.join(prime_lists))


n = int(input())
nums = input().split()

reverse(n, nums)