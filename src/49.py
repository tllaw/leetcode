class Solution:
    def groupAnagrams(self, strs):
        m = dict()

        for s in strs:
            key = "".join(sorted(s))
            m[key] = m.get(key, []) + [s]

        return m.values()
