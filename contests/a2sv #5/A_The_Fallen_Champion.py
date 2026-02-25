win, time = map(int, input().split())
n = int(input())
is_best = True

for _ in range(n):
    wi, ti = map(int, input().split())

    if win < wi:
        is_best = False
        break
    elif wi == win:
        if ti < time:
            is_best = False
            break


if is_best:
    print("The Champion Saves the Accused")
else:
    print("The Fallen Champion")