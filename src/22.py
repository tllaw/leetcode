class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(l, r, curr):
            if l + r == 2 * n:
                result.append(curr)
                return

            if l < n:
                curr += "("
                backtrack(l + 1, r, curr)
                curr = curr[:-1]

            if r < l:
                curr += ")"
                backtrack(l, r + 1, curr)
                curr = curr[:-1]

        backtrack(0, 0, "")
        return result
