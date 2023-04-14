class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                lives = 0
                r = [max(i - 1, 0), min(i + 1, m - 1)]
                c = [max(j - 1, 0), min(j + 1, n - 1)]

                for x in range(r[0], r[1] + 1):
                    for y in range(c[0], c[1] + 1):
                        if i == x and j == y:
                            continue

                        lives += board[x][y] & 1

                if lives == 3 or (board[i][j] == 1 and lives == 2):
                    board[i][j] += 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
