class Solution:
    def getRow(self, rowIndex):
        rows = [[], [1]]

        for i in range(rowIndex):
            rows[0] = rows[1]
            rows[1] = [0 for j in range(len(rows[0]) + 1)]

            for j, v in enumerate(rows[0]):
                rows[1][j] += rows[0][j]
                rows[1][j + 1] += rows[0][j]

        return rows[1]
