class Solution:
    def wordPattern(self, pattern, s):
        hashmap = [None for _ in range(26)]
        pattern, s = list(pattern), s.split()

        if len(pattern) != len(s):
            return False

        for i, p in enumerate(pattern):
            c = ord(p) - ord("a")

            if not hashmap[c]:
                hashmap[c] = s[i]
            elif hashmap[c] != s[i]:
                return False

        return len(set(pattern)) == len(set(s))
