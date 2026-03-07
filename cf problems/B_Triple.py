from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq_Count = Counter(a)
    
    candidates = [num for num, count in freq_Count.items() if count >= 3]

    print(max(candidates) if candidates else -1)