n = int(input())

cnt = 0

while n != 1:
    if n%6==0:
        n1 = n//3
        cnt += 1
        print(1)

    elif n%3==1:
        n = n-1
        

    elif n%2==1:
        n = n-1
        print(2)

    else:
        n = n-1
        cnt += 1
        print(3)
    

print(cnt)