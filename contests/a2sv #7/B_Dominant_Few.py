t = int(input())

for _ in range(t):
    n = int(input())
    skill = list(map(int, input().split()))
    skill.sort(reverse=True)
    possible = False

    for k in range(1, n):
        elite = sum(skill[:k])
        crowd = sum(skill[k:])

        if k < n - k and elite > crowd:
            possible = True
            break

    print("YES" if possible else "NO")