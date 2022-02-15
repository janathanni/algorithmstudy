x, y, w, h = map(int, input().split())

# (w, 0), (0, h), (0, 0), (w, h)

lines = [x, y, w-x , h-y]

print(min(lines))

