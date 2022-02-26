while True:

    n = int(input())

    if n == 0:
        break
    
    nn = 2*n

    num_list = [0 for i in range(0, (nn+1))]

    p = []

    for i in range(2, (nn+1)):
        if num_list[i] == 0:
            if n < i <= nn:
                p.append(i)
            for j in range(i, (nn+1), i):
                num_list[j] = 1
        

    print(len(p))

        


