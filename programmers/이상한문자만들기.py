from re import A


def solution(s):
    words = s.split()

    new_words = []

    for word in words:
        answer = ''
        for i in range (0, len(word)):
            if i%2 == 1:
                answer += word[i].lower()
            else:
                answer += word[i].upper()
            
        new_words.append(answer)
    
    return ' '.join(new_words)

print(solution("niniz nini hehehe"))