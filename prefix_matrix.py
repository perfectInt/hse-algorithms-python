n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

prefix_matrix = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            prefix_matrix[i][j] = matrix[i][j] + prefix_matrix[i - 1][j] + prefix_matrix[i][j - 1] - prefix_matrix[i - 1][j - 1]
        elif i > 0 and j == 0:
            prefix_matrix[i][j] = matrix[i][j] + prefix_matrix[i - 1][j]
        elif i == 0 and j > 0:
            prefix_matrix[i][j] = matrix[i][j] + prefix_matrix[i][j - 1]
        else:
            prefix_matrix[i][j] = matrix[i][j]

for i in range(n):
    print(*prefix_matrix[i])

