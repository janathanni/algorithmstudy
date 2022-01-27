nums = [str(i) for i in range (0,10)]

strings = input()

numstr = ''

for string in strings:
    if string in nums:
        numstr = numstr + string

    else:
        continue

cnt = 0

for divisor in range (1, int(numstr)+1):

    if int(numstr) % divisor == 0 :
        cnt +=1
    
    else:
        continue

print(int(numstr))
print(cnt)
#이제 약수의 개수는 어떻게 구한담?