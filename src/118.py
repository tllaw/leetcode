class Solution:
    def generate(self, numRows):
        result = [[1]]

        for i in range(1, numRows):
            result.append([0 for j in range(i + 1)])

            for j in range(i):
                result[i][j]     += result[i - 1][j]
                result[i][j + 1] += result[i - 1][j]

        return result
