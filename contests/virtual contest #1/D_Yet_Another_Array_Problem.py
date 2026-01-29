import math

t = int(input())

for _ in range(t):
    n = int(input())
    nums = map(int, input().split())

    ans = 2
    for x in nums:
        if x % 2 == 0:
            ans = 1
            break
    
    print(ans)
