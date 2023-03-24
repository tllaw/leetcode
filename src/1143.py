class Solution:
    def longestCommonSubsequence(self, p, q):
        # return self.recursion(p, q, {})
        return self.iteration(p, q)

    def recursion(self, p, q, d):
        if not p or not q:
            return 0

        if (p, q) not in d:
            if p[0] == q[0]:
                d[(p, q)] = 1 + self.recursion(p[1:], q[1:], d)
            else:
                x = self.recursion(p[1:], q, d)
                y = self.recursion(p, q[1:], d)
                d[(p, q)] = max(x, y)

        return d[(p, q)]

    def iteration(self, p, q):
        m, n = len(p), len(q)
        r = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                c, d = p[i], q[j]

                if c == d:
                    r[i + 1][j + 1] = r[i][j] + 1
                else:
                    r[i + 1][j + 1] = max(r[i + 1][j], r[i][j + 1])

        return r[-1][-1]
