n, k = map(int, input().split())

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    print(*arr)