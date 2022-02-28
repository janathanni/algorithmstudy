from collections import Counter

num = int(input())

cards = Counter(map(int, input().split()))

print(cards[num])