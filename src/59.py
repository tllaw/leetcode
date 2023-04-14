class Solution:
    def generateMatrix(self, n):
        result = [[None for _ in range(n)] for _ in range(n)]
        x, y, i, j, result[0][0] = 1, 0, 0, 0, 1

        for m in range(2, n * n + 1):
            i += y
            j += x
            result[i][j] = m

            outBoundX = x != 0 and (j >= n - 1 or j <= 0 or result[i][j + x] != None)
            outBoundY = y != 0 and (i >= n - 1 or i <= 0 or result[i + y][j] != None)
            if outBoundX or outBoundY:
                x, y = -y, x

        return result
