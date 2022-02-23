def solution(s):

    answer = s[::] 
    alph_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3',
    'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    for k, v in alph_dict.items():
        if k in s:
            answer = answer.replace(k, v)

    return int(answer)


print(solution("one4seveneight"))