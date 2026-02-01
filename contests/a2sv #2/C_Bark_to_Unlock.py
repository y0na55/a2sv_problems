

password = input().split()

n = int(input())
full_words = []
bark = []

for _ in range(n):
    words = input().split()
    full_words.append(words)

for x in full_words:
    bark.append(*x)

barks = ''.join(bark)

# print(barks)

# if password in barks:
#     print("YES")
# else:
#     print("NO")

for i in range(len(barks)):
    char = barks[i: i+1]

    # print(char)

    
    if char == password:
        print("YES")
        break
    else:
        print("NO")
        break

# if password in full_words:
#     print("YES")

# print("NO")