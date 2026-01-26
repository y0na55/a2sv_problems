# n, k = map(int, input().split())

# res = []

# for i in range(n):
#     if i % 2 == 1:
#         res.append(i)

# for j in range(n):
#     if j % 2 == 0:
#         res.append(j)

# print(res[k-1])

# this fells the test cause when checking long numbers it will take a long time and also lot of memory
# that's why its felling on the 5th test

# odd group: 1, 3, 5, 7, 9 (pos 1, 2, 3, 4, 5)
# even group: 2, 4, 6, 8, 10 (pos 6, 7, 8, 9, 10)
# so i just need to take the mid point and then check if k is before the mid point or after
# if its  that means we are looking for an odd number return(2*k-1)th element cause eg: if k = 2 ans = 3. 
# if not we are looking for an even number so shift the k so that it starts from 1 then return (2*k) eg: if k = 6 we shift it to k to be 1 then 
# 2 * 1 = 2 and we return 2 

n, k = map(int, input().split())

mid = (n + 1) // 2

if k <= mid:
    print(2 * k - 1)
else:
    k = k - mid
    print(2 * k)

