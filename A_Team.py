n = int(input())
ans = 0

for _ in range(n):
    list_input = list(map(int, input().split()))
    if sum(list_input) >= 2:
        ans += 1
    
print(ans)