# n, k = map(int, input().split()) # n 카드수 , k번째 큰 값
# cards = list(map(int,input().split())) # 뽑은 카드들

# total_list = set()

# for i in range (0, len(cards)):
#     for j in range (i+1, len(cards)):
#         for k in range (j+1, len(cards)):
#                 total_list.add(cards[i]+cards[j]+cards[k])

# total_list = sorted(list(total_list))

# print(total_list[-k])

n, k =map(int, input().split())
cards = list(map(int, input().split()))

res = set()

for i in range (0, len(cards)):
    for j in range (i+1, len(cards)):
        for k in range (j+1, len(cards)):
            total_list.add(cards[i]+cards[j]+cards[k])

res = list(res)
res.sort(reverse=True)
print(res[k-1])