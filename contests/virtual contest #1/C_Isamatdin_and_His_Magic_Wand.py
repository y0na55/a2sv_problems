test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    toys = list(map(int, input().split()))
    

    # for i in range(n-1):
    #     if toys[i] % 2 != toys[i+1] % 2:
    #         toys.sort()  #0log(n)
    # print(*toys)

    # worst case becomes O(n² log n) 
    # so i gotta sort out of the loop to minimize the time complexity

    has_even = False
    has_odd = False

    for x in toys:
        if x % 2 :
            has_even = True
        else:
            has_odd = True

    if has_even and has_odd:
        toys.sort()
    
    print(*toys)