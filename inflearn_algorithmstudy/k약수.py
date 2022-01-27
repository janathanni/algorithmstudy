# n, k = map(int, input().split())
# h = 0
# divisor = 1
# divisor_memory = 0

# while h<k:
#     if n%divisor == 0:
#         h += 1
#         divisor_memory = divisor
#         divisor += 1

# if h != k :
#     print(-1)

# else:
#     print(divisor_memory)

n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i ==0 :
        cnt+=1
    if cnt==k:
        print(i)
        break

else:
    print(-1)
