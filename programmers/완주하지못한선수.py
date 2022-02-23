from collections import Counter

def solution(participant, completion):
    participant2 = Counter(participant)
    completion2 = Counter(completion)

    total = participant2 - completion2

    not_comp = ''

    for k, v in total.items():
        if v == 1:
            not_comp = k

    return k