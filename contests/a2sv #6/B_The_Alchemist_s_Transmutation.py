t = int(input())

for _ in range(t):
    n = int(input())
    crystals = list(map(int, input().split()))
    e = int(input())

    if crystals[0] >= crystals[-1]:
        if crystals[-1] < 0 and e < 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
