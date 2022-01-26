nums = [str(i) for i in range (0,10)]

strings = input()

numstr = ''

for string in strings:
    if string in nums:
        numstr = numstr + string

    else:
        continue

print(int(numstr))