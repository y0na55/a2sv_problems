# both alice and betty will get biscuit
# if there is remaining biscuit after they get their share alice will take the remaining once 
# all the biscuit needs to add up to the total buscuit

# find a way to find number of ways a + b = biscuits and also a > b

# get the mid and return 




t = int(input())

for _ in range(t):
    n = int(input())

    print((n-1) - (n // 2))