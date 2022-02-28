tscore = 0

for _ in range(0,5):
    score = int(input())

    if score <= 40:
        tscore += 40
    
    else:
        tscore += score


print(tscore//5)