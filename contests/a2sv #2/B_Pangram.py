n = int(input())
word = input().lower()

word_set = set(word)

if len(word_set) < 26:
    print("NO")
else:
    print("YES")



