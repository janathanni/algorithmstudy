clock, minute = map(int, input().split())

cook = int(input())

clock2 = (minute + cook)//60

clock = clock + clock2

minute2 = (minute+cook)%60

if clock >= 24:
    clock -= 24

print(clock, minute2)