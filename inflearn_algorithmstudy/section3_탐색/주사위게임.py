# n = int(input())

# prices = []

# for _ in range (0, n):
#     a, b, c = map(int, input().split())

#     if a == b and b == c :
#         prices.append(10000 + (a * 1000))
    
#     elif a != b != c:
#         prices.append(max(a, b, c)*100)
    
#     else:
#         prices.append(min(a,b,c)*100 + 1000)

# print(max(prices))


#Answer

n=int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a==b and b==c:
        money = 10000+a*1000
    
    elif a == b or a==c:
        money = 1000 + (a*100)
    
    elif b==c:
        money=1000+(b*100)
    
    else:
        money = c*100
    
    if money > res:
        res = money