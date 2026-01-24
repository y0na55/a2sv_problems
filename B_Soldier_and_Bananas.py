# k: cost of the first banana
# n: initial money the soldier has
# w: number of bananas he wants to buy
k, n, w = map(int, input().split())

cost, desire, money = map(int, input().split())

if money < desire:
    print(desire - money)
else:
    print(0)

