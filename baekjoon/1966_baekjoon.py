from collections import deque
import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    total_num, quest = map(int, sys.stdin.readline().split())
    prints = deque(map(int, sys.stdin.readline().split()))
    prints2 = prints.copy()
    cnt = 1
    
    max_num = max(prints)

    for i in range(len(prints)):
        if prints2[i] 