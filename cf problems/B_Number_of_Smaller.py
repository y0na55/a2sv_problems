n, m = list(map(int, input().split()))

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

first = 0
smaller_nums = []


for second in range(len(list_2)): 
    while first < len(list_1) and list_1[first] < list_2[second]: 
        first += 1

    smaller_nums.append(first)


print(' '.join(map(str, smaller_nums)))
