class Solution:
    def solveNQueens(self, n):
        result  = []
        board   = [["."] * n for _ in range(n)]
        c, d, a = [], [], []

        def is_occupied(i, j):
            return (j in c) or (i + j in d) or (i - j in a)

        def occupy(i, j):
            board[i][j] = "Q"
            c.append(j)
            d.append(i + j)
            a.append(i - j)

        def deoccupy(i, j):
            board[i][j] = "."
            c.pop()
            d.pop()
            a.pop()

        def backtrack(i):
            if i == n:
                result.append(["".join(r) for r in board])
                return

            for j in range(n):
                if not is_occupied(i, j):
                    occupy(i, j)
                    backtrack(i + 1)
                    deoccupy(i, j)

        backtrack(0)
        return result
