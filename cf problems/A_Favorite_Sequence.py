t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    left, right = 0, len(arr)-1
    result = []

    while left < right:
        result.append(arr[left])
        result.append(arr[right])
        left += 1            
        right -= 1
    if left == right:
        result.append(arr[left])
        
    print(*result)