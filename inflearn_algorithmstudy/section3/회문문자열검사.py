# n = int(input())
# cnt = 1
# for _ in range (n):
#     string = list(input().lower())
    
#     if string == string[::-1]:
#         print(f'{cnt}# YES')

#     else:
#         print(f'{cnt}# NO')
    
#     cnt += 1


#Answer

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)

    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    
        else:
            print("#%d YES" %(i+1))
