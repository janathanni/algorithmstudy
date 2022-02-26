n = int(input())

n_array = list(map(int, input().split()))

n_array.sort()

m = int(input())

m_array = list(map(int, input().split()))

cnt = 1

for i in m_array:
    lt = 0
    rt = len(n_array)

    while lt <= rt:

        middle = (lt+rt)//2
        cnt *= 2
    
        if i == n_array[middle]:
            print(1)
            break

        elif cnt > n:
            print(0)
            break

        elif i > n_array[middle]:
            lt = middle+1
            
        else:
            rt = middle-1
 


    