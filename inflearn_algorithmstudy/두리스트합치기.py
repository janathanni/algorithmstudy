length_1 = int(input())
list_1 = input()

length_2 = int(input())
list_2 = input()

total_list = (list_1 + ' ' + list_2).split()
total_list.sort()
print(total_list)

print(' '.join(total_list))