n, k = input().split()
nums = list(map(int, input().split()))
nums.sort()
first_time = True


n = int(n)
k = int(k)


if first_time:
    minn = nums[0]
    first_time = False
    print(minn)


for i in range(k-1):
    i = 1
    print(minn - i)