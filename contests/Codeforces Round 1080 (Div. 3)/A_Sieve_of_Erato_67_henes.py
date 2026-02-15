t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))


    if 67 in nums:
        print("YES")
    else:
        print("NO")    

    # found = False
    # for i in range(len(nums)):
    #     for j in range(len(nums)):

    #         if nums[i] * nums[j] == 67:
    #             found = True
    #             break

    #     if found:
    #         break
    
    # if found:
    #     print("YES")
    # else:
    #     print("NO")