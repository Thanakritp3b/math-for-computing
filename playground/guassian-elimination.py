matrix =  [[1, 1, 1],
           [3, 2, 1],
           [2, -1, 4]]

result = [[6],
       [10],
       [12]]


def gaussian_elimination(matrix, result):
    n = len(matrix)
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            k = -1 * matrix[j][i] / matrix[i][i]
            # print (k)
            for l in range(i, n):
                matrix[j][l] += k * matrix[i][l]
            result[j][0] += k * result[i][0]
            # print(matrix)
            # print(result)
    ans.append(result[n-1][0] / matrix[n-1][n-1])
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            result[i][0] -= matrix[i][j] * ans[n - j - 1]
        ans.append(result[i][0] / matrix[i][i])
    return ans[::-1]


print(gaussian_elimination(matrix, result))


