t = int(input())

for _ in range(0,t):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))[s-1:e]
    num = sorted(nums)[k-1]
    print(num)

    