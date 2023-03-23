class Solution:
    # d = {}

    def uniquePaths(self, m, n):
        # return self.recursion(m, n)
        return self.iteration(m, n)

    def recursion(self, m, n):
        if m == 1 or n == 1:
            return 1

        m, n = max(m, n), min(m, n)
        if (m, n) not in self.d:
            self.d[m, n] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

        return self.d[m, n]

    def iteration(self, m, n):
        m, n = min(m, n), max(m, n)
        r = [1] * m

        for i in range(n - 1):
            for j in range(1, m):
                r[j] += r[j - 1]

        return r[-1]
