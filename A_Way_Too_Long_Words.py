t = int(input())

for _ in range(t):
    word = input()

    if len(word) > 10:
        a = word[0]
        b = str(len(word)-2)
        c = word[-1]

        char = a + b + c
        print(char)
    else:
        print(word)