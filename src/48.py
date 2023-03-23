class Solution:
    def rotate(self, matrix):
        # self.rotate_four_cells(matrix)
        self.transpose_and_reflect(matrix)

    def rotate_four_cells(self, matrix):
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                p, q = n - i - 1, n - j - 1
                temp = matrix[i][j]
                matrix[i][j] = matrix[q][i]
                matrix[q][i] = matrix[p][q]
                matrix[p][q] = matrix[j][p]
                matrix[j][p] = temp

    def transpose_and_reflect(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                k = n - j - 1
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
