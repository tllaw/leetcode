class Solution:
    def longestPalindrome(self, s):
        hashmap, odd = [0 for i in range(128)], 0

        for x in s:
            hashmap[ord(x)] += 1

        for x in hashmap:
            odd += x % 2

        return len(s) - (odd - 1 if odd > 1 else 0)
