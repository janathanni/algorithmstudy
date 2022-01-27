# import collections

# n, m = map(int, input().split())

# added = []

# for i in (1, n+1):
#     for j in (1, m+1):
#         added.append(i+j)

# total = collections.Counter(added)
# total_max = sorted([k for k,v in total.items() if max(total.values()) == v ])
# print(total_max)


#--------

n, m = map(int, input().split())

added = [0 for i in range(0, (n+m)+3)]
for i in (1, n+1):
    for j in (1, m+1):
        added[i+j] += 1

for i in range(n+m+3):
    if added[i] == max(added):
        print(i, end=' ')

print(added.index(max(added)))