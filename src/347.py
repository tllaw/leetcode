class Solution:
    def topKFrequent(self, nums, k):
        # return self.quick_select(nums, k)
        # return self.hash_dict(nums, k)
        return self.bucket(nums, k)

    def quick_select(self, nums, k):
        m = {}
        p = []

        for n in nums:
            m[n] = m.get(n, 0) + 1

        for h, v in m.items():
            p.append([v, h])

        i, j, k = 0, len(p) - 1, len(p) - k

        while True:
            o = i

            for z in range(i, j):
                if p[z][0] < p[j][0]:
                    p[z], p[i] = list(p[i]), list(p[z])
                    i += 1

            p[i], p[j] = list(p[j]), list(p[i])

            if i == k:
                return [p[z][1] for z in range(i, len(p))]

            if i < k:
                i = i + 1
            else:
                i, j = o, i - 1

    def hash_dict(self, nums, k):
        m, n = {}, {}

        for x in nums:
            f = m.get(x, 0)
            m[x] = f + 1
            n[f + 1] = n.get(f + 1, []) + [x]

            if f:
                n[f].remove(x)

        r = [item for elements in n.values() for item in elements]
        return r[len(r) - k:]

    def bucket(self, nums, k):
        d, m = {}, 0

        for n in nums:
            d[n] = d.get(n, 0) + 1
            m = max(m, d[n])

        b = [[] for _ in range(m + 1)]

        for e in d.items():
            b[e[1]].append(e[0])

        r = []

        while k:
            if b[m]:
                r.append(b[m].pop())
                k -= 1
            else:
                m -= 1

        return r
