from imaplib import Int2AP
from operator import itemgetter
from collections import deque

import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    total_num, quest = map(int, sys.stdin.readline().split())
    prints = deque()
    case_list = list(map(int, sys.stdin.readline().split()))

    for v, i in enumerate(case_list):
        prints.append((v,i))
    
    case_list = sorted(case_list)
    prints = sorted(prints, key = itemgetter(0))
    cnt = 0

    while 
        if case_list == prints[0][1]:

        tmp1= prints.leftpop()
        prints.append(tmp1)
    
        

    
