n, m = list(map(int, input().split()))
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

first, second = 0, 0
result = []
while first < len(arr_1) and second < len(arr_2): 
    if arr_1[first] <= arr_2[second]: 
        result.append(arr_1[first])
        first += 1
    else: 
        result.append(arr_2[second])
        second += 1

result.extend(arr_1[first:])
result.extend(arr_2[second:])

print(' '.join(map(str, result)))
