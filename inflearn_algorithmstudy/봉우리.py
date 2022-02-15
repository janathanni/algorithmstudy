n = int(input())

mountains = []

for _ in range (n):
    nums = list(map(int, input().split()))
    mountains.append(nums)

#current1 => index of lists. current2 => index of list.

#if current1 == 0 and current2 == 0 // up and left is 0.
#elif current2 == 0 // left is 0.
#elif current1 == last and current2 ==0 // down and left is 0.

#elif current1 == 0 and current == last //up and right is 0.
#elif current2 == last  // right is 0.
#elif current1 == last and current2 == last // down and right is 0.

#buds[current1-1][current2] up
#buds[current1+1][current2] down
#buds[current1][current2-1] left
#buds[current1][current2+1] right

cnt = 0

for i in range (n):
    for j in range (n):
        
        nums = []

        if i == 0 and j == 0:
            nums.append(mountains[i][j], mountains[i+1][j], mountains[i][j+1])
            if max(nums) == mountains[i][j]:
                cnt+=1

        elif i == 0 and j == 0:
            nums.append(mountains[i][j])
    




