n = int(input())

n_array = list(map(int, input().split()))

n_array.sort()

m = int(input())

m_array = list(map(int, input().split()))

for i in m_array:
    cnt = 2
    lt = 0
    rt = len(n_array)

    while lt <= rt:

        middle = (lt+rt)//2
        
        if cnt > n:
            print(0)
            break

        if cnt <= n:
            if i == n_array[middle]:
                print(1)
                break

            elif i > n_array[middle]:
                lt = middle+1
                cnt *= 2
            
            else:
                rt = middle-1
                cnt *= 2

    