def solve():
    t = int(input())
    for _ in range(t):
        s, k, m = map(int, input().split())
        full_cycles = m // k
        remainder = m % k
        
        if full_cycles % 2 == 0:
            print(max(0, s - remainder))
        else:
            print(max(0, remainder))