n = int(input())

n_array = list(map(int, input().split()))

n_array.sort()

m = int(input())

m_array = list(map(int, input().split()))

for i in m_array:
    lt = 0
    rt = len(n_array)

    while lt <= rt:
        middle = (lt+rt)//2

        if middle >= n or middle < 0:
            print(0)
            break

        if i == n_array[middle]:
            print(1)
            break
        
        if i > n_array[middle]:
            lt = middle+1
           
        else:
            rt = middle-1


    