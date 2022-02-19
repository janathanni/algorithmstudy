n = int(input())

words = []

for _ in range(n):
    word=input()
    if word in words:
        continue

    else:
        words.append(word)

words.sort(key = lambda word : (len(word), word))

for i in words:
    print(i)