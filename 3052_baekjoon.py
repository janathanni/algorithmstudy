lis=[]

for i in range(0, 10):
    n = int(input())
    lis.append(n%42)


set_lis = set(lis)

print(len(set_lis))