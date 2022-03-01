import sys

n, k = map(int, sys.stdin.readline().split())

s = k - 1

seq = [str(i) for i in range(1, n+1)]
j_seq = []

while True:
    j_seq.append(seq[s])
    del seq[s]
    if seq:
        s = (s+k-1)%len(seq)
    else:
        break

print('<'+ ', '.join(j_seq) +'>')