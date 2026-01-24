num = int(input())

for i in range(num):
    char = input()
    if len(char) > 10:
        a = char[0]
        b = str(len(char) - 2)
        c = char[-1]

        result = a + b + c
        print(result)
    else:
        print(char)
