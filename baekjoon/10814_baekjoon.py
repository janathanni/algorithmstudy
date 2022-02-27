from operator import itemgetter
import sys
from operator import itemgetter

n = int(sys.stdin.readline())

lists = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    lists.append((int(age), name))


lists2 = sorted(lists, key=itemgetter(0))

for age, name in lists2:
    print(age, name)