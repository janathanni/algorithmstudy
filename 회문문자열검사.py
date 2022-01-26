n = int(input())
cnt = 1
for _ in range (n):
    string = list(input().lower())
    
    if string == string[::-1]:
        print(f'{cnt}# YES')

    else:
        print(f'{cnt}# NO')
    
    cnt += 1

