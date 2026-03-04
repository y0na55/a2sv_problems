t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    min_value = a[0]
    count = 0
    for num in a:
        if num == min_value:
            count += 1

    if count % 2 != 0:
        print("YES")
    else:
        print("NO")
