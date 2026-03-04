n, m = list(map(int, input().split()))
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

count = 0 
for first in range(len(list_1)): 
    second = 0
    while second < len(list_2): 
        if list_1[first] == list_2[second]: 
            count += 1
        second += 1

print(count)
