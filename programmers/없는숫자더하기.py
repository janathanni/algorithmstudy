from collections import Counter

def solution(numbers):
    list_dic = Counter([i for i in range(0,10)])
    list_dic2 = Counter(numbers)

    answer_dic = list_dic - list_dic2

    total = 0

    for k, v in answer_dic.items():
        if v == 1:
            total += k

    return total

print(solution([5,8,4,0,6,7,9]))