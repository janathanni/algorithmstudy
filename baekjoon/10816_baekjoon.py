n = int(input())
n_array = list(map(int, input().split()))

n_array.sort()

m = int(input())
m_array = list(map(int, input().split()))

cards_num = []

for i in m_array:

    lt = 0
    rt = len(n_array)

    cnt = 0

    while lt <= rt:

        mid = (lt+rt)//2

        if i == n_array[mid]:
            cnt += 1
        
        elif i < n_array[mid]:
            rt = mid-1
        
        else:
            lt = mid+1
    
    cards_num.append(cnt)

print(cards_num)