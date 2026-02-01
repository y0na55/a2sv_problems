import sys

input = sys.stdin.readline

n = int(input())

words = input().split()

word = ''.join(words)
count = 0


# print(word)

for char in word:
    if char.isupper():
        print("YES")
        break
    else:
        print("NO")
        break

# if count:
#     print("YES")

# else:
#     print("NO")



# if any(char.isupper() for char in words):
#     print("YES")

# print("NO")


# any(char.isupper() for char in word)

# if any(char.isupper() for char in words):
#     print("YES")

# print("NO")


# if all(char.isupper() for char in words):
#     print("YES")

# print("NO")


# count = 0

# for char in words:
#     if any(char.isupper()):
#         count += 1
#         break

# if count:
#     print("YES")

# print("NO")



# for char in words:
#     if any(char.isupper()):
#         print("Yes")
#         break
#     else:
#         print("NO")
