t = int(input())

for _ in range(t): 
    n = int(input())
    
    if n > 3  and n % 2 == 0: 
        print(0)
    elif n > 3 and n % 2 == 1: 
        print(1)
    else: 
        print(n)
