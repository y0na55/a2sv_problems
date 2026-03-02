t = int(input())

for _ in range(t):
    n = int(input())
    crystals = list(map(int, input().split()))
    energy = int(input())

    if min(crystals) <= energy <= max(crystals):
        print("YES")
    else:
        print("NO")