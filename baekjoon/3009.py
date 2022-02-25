list1 = []
list2 = []

a, b = input().split()
c, d = input().split()
e, f = input().split()

list1.extend([a,c,e])
list2.extend([b,d,f])

list_set1 = set(list1)
list_set2 = set(list2)

coord = ''

for i in list_set1:
    if list1.count(i) == 1:
        coord = coord + i

for i in list_set2:    
    if list2.count(i) == 1:
        coord = coord + ' ' + i


print(coord)