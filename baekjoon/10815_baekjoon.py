from collections import Counter
import sys
n = int(input())
cards = Counter(sys.stdin.readline().rstrip().split())

n2 = int(input())

m_card = sys.stdin.readline().rstrip().split()

for i in m_card:
    if i in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')