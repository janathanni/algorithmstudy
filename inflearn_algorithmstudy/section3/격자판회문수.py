board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        
        tmp2 = [board[i+k][j] for k in range(0,5)]

        if tmp2 == tmp2[::-1]:
            cnt += 1

print(cnt)