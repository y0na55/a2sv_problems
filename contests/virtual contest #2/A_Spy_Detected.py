from collections import Counter
t = int(input())

for _ in range(t):
    len_arr = int(input())
    arr = list(map(int, input().split()))

    count = Counter(arr)
    num = None
    for count, rep in count.items():
        if rep == 1:
            num = count
    print(arr.index(num)+1)