import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range (n):
    word = sys.stdin.readline()
    alph_list = [word[0]]
    check = True
    for i in range(1, len(word)):        
        if word[i-1] == word [i]:
            continue

        elif word[i] in alph_list:
            break
                
        else:
            alph_list.append(word[i])
    else:
        cnt +=1

print(cnt)