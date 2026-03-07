n = int(input())

cards = list(map(int, input().split()))

left , right = 0, n - 1
players = [0, 0]
current = 0

while left <= right:
    if cards[right] >= cards[left]:
        chosen = cards[right]
        right -= 1
    else:
        chosen = cards[left]
        left += 1

    players[current] += chosen
    current = 1 - current
    
    
print(players[0], players[1])