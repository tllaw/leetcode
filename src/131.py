class Solution:
    def partition(self, s):
        # return self.build_palindromes(s)
        return self.check_palindromes(s)

    # build all possible palindromes first,
    # then perform partition using backtrakcing
    def build_palindromes(self, s):
        result = []
        palindromes = [[] for _ in s]

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].append(s[l:r+1])
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].append(s[l:r+1])
                l -= 1
                r += 1

        def backtrack(curr, i):
            if i == len(s):
                result.append(list(curr))
                return

            for el in palindromes[i]:
                curr.append(el)
                backtrack(curr, i + len(el))
                curr.pop()

        backtrack([], 0)
        return result

    # perform partition using backtracking
    # and check if the subtring is palindrome in time
    def check_palindromes(self, s):
        result = []
        dp = [[None for j in s] for i in s]

        def is_palindrome(i, j):
            if dp[i][j] != None:
                return dp[i][j]

            while i < j:
                if s[i] != s[j]:
                    dp[i][j] = False
                    return dp[i][j]
                i += 1
                j -= 1

            dp[i][j] = True
            return dp[i][j]

        def backtrack(curr, i):
            if i == len(s):
                result.append(list(curr))
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    curr.append(s[i:j+1])
                    backtrack(curr, j+1)
                    curr.pop()

        backtrack([], 0)
        return result
