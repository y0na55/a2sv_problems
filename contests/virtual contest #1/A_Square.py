test_cases = int(input())

for num in range(test_cases):
    side_a, side_b, side_c, side_d = map(int, input().split())
    if side_a == side_b == side_c == side_d:
        print("YES")
    else:
        print("NO")