class Solution:
    def minPathSum(self, grid):
        # return self.recursion(grid, len(grid) - 1, len(grid[0]) - 1, {})
        return self.iteration(grid)

    def recursion(self, grid, m, n, d):
        if m < 0 or n < 0:
            return math.inf

        if m == 0 and n == 0:
            return grid[0][0]

        if (m, n) not in d:
            up      = self.recursion(grid, m - 1, n, d)
            left    = self.recursion(grid, m, n - 1, d)
            d[m, n] = min(up, left) + grid[m][n]

        return d[m, n]

    def iteration(self, grid):
        m, n = len(grid), len(grid[0])
        r    = [inf, 0] + [inf] * (n - 1)

        for i in range(m):
            for j in range(1, n + 1):
                r[j] = min(r[j - 1], r[j]) + grid[i][j - 1]

        return r[-1]
