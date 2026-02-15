t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    possible = True
    
    for i in range(n//2 - 1, -1, -1):
        left = 2 * i + 1
        
        # If left child exists and parent > left child
        if left < n and nums[i] > nums[left]:
            nums[i], nums[left] = nums[left], nums[i]
    
    # check if the array is sorted
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            possible = False
            break
    
    print("YES" if possible else "NO")