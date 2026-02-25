from collections import defaultdict

n = int(input())
pair_days = defaultdict(set)


for day in range(n):
    m = int(input())

    for _ in range(m):
        s, h = input().split()
        h = int(h)

        pair_days[(s, h)].add(day)

cheating = False
required_days = (80 * n + 99) // 100


for days_set in pair_days.values():
    if len(days_set) >= required_days:
        cheating = True
        break

print("YES" if cheating else "NO")