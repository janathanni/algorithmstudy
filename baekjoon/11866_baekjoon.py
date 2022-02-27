n, m = map(int, input().split())

n_list = [i for i in range(1, n+1)]

# m-1  -> m-1 + 3 -> m -1 + 3 + 3

d = 0
cnt = 1
m_total = 2

while cnt < n:
    print(n_list[m_total])

    m_total = (m_total+3-d)%n
    cnt += 1
    d += 1