matrix = [list(map(int, input().split())) for _ in range(5)]
x = None
y = None

for i in range(len(matrix)):
    for j in range(len(matrix[0])):

        if matrix[i][j] == 1:
            x = i
            y = j

true_x = abs(x-2)
true_y = abs(y-2)

pos = true_x + true_y

print(pos)