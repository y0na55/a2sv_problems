t = int(input())

for _ in range(t):
    n = int(input())
    a, b = input().split()

    a_even, a_odd = [], []
    b_even, b_odd = [], []

    for i in range(n):
        if i % 2 == 0:
            a_even.append(a[i])
            b_even.append(b[i])
        else:
            a_odd.append(a[i])
            b_odd.append(b[i])

    if sorted(a_even) == sorted(b_even) and sorted(a_odd) == sorted(b_odd):
        print("YES")
    else:
        print("NO")
