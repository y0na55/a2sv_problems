n, k = map(int, input().split())

res = []

for i in range(n):
    if i % 2 == 1:
        res.append(i)

for j in range(n):
    if j % 2 == 0:
        res.append(j)

print(res[k-1])