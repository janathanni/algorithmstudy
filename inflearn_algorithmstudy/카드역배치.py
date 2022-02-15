# cards = [i for i in range(1, 21)]

# for batch in range (10):
#     a , b = map(int, input().split())

#     cards[a-1:b] = cards[a-1:b][::-1]

# print(cards)

a, b= map(int, input().split())
print(a, b)

a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

print(a)