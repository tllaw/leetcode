class Solution:
    def intervalIntersection(self, p, q):
        i, j, m, n, r = 0, 0, len(p), len(q), []

        while i < m and j < n:
            c, d = max(p[i][0], q[j][0]), min(p[i][1], q[j][1])
            if c <= d:
                r.append([c, d])

            if p[i][1] < q[j][1]:
                i += 1
            else:
                j += 1

        return r
