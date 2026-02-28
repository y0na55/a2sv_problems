t = int(input())

for _ in range(t):
    n = int(input())
    decorations = list(map(int, input().split()))

    decorations.sort()
    needed = 3
    minn  = float('inf')
    num = 0
    
    for i in range(n - 2):
        minn = min(minn, (decorations[i+2] - decorations[i]))


    # for i in range(1, n):
    #     if decorations[i-1] == decorations[i]:
    #         num = decorations[i]
    #         needed -= 2

    # if needed == 1:
    #     for i  in range(n-2):
    #         minn = min(minn, int(abs(decorations[i+1] - decorations[i])))

    # if needed == 3:
    #     minn = 0
    #     middle = (0 + sum(decorations)) // n
    #     idx = (n // 2) + 1

    #     i = 1
    #     j = 1
    #     for x in range(n-1):
    #         if decorations[idx - 1] + i != middle:
    #             minn += 1
    #             i += 1

    #     for x in range(n - 3):
    #         if decorations[idx  + 1] - j != middle:
    #             minn += 1
    #             j += 1

    print(minn)
