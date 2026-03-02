t = int(input())

for _ in range(t):
    n = int(input())
    crystals = list(map(int, input().split()))
    Energy_level = int(input())

    if min(crystals) <= Energy_level <= max(crystals):
        print("YES")
    else:
        print("NO")
