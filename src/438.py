class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        h, b, r = [0] * 26, True, []

        for i in range(len(p)):
            h[ord(p[i]) - ord('a')] += 1
            h[ord(s[i]) - ord('a')] -= 1

        for i in h:
            if i:
                b = False
                break

        if b:
            r.append(0)

        for i in range(len(p), len(s)):
            h[ord(s[i - len(p)]) - ord('a')] += 1
            h[ord(s[i]) - ord('a')] -= 1

            b = True
            for j in h:
                if j:
                    b = False
                    break

            if b:
              r.append(i - len(p) + 1)

        return r
