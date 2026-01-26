# k: cost of the first banana
# n: initial money the soldier has
# w: number of bananas he wants to buy
k, n, w = map(int, input().split())

total_cost = 0

# Loop from 1 to w 
for i in range(1, w + 1):
    total_cost += i * k

borrow = total_cost - n

if borrow > 0:
    print(borrow)
else:
    print(0)

