def solution(phone_number):
    answer = ''.join(['*' for _ in phone_number[:-4]]) + phone_number[-4:]
    return answer

print(solution('01033334444'))