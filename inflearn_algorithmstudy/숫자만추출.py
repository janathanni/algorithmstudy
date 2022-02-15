# nums = [str(i) for i in range (0,10)]

# strings = input()

# numstr = ''

# for string in strings:
#     if string in nums:
#         numstr = numstr + string

#     else:
#         continue

# print(int(numstr))


#Anwer

s = input()

res = 0

for x in s:
    if x.isdecimal():
        res = res*10 + int(x)
print(res)

cnt = 0

for i in range(1, res+1):
    if res%i==0:
        cnt+=1

print(cnt)