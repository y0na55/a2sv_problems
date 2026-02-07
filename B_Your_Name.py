t = int(input())

for _ in range(t):
    name_len = int(input())
    name = list(map(str, input().split()))
    
    first_name = name[0]
    second_name = name[1]
    first = sorted(first_name)
    second = sorted(second_name)

    if first == second:
        print("YES")
    else:
        print("NO")