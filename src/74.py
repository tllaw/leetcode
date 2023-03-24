class Solution:
    def searchMatrix(self, matrix, target):
        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        i, j, r = 0, len(matrix), -1

        while i <= j:
            m = (i + j) // 2

            if matrix[m][0] <= target and target <= matrix[m][-1]:
                r = m
                break
            elif target < matrix[m][0]:
                j = m - 1
            else:
                i = m + 1

        i, j = 0, len(matrix[r]) - 1

        while i <= j:
            m = (i + j) // 2

            if matrix[r][m] == target:
                return True

            if target < matrix[r][m]:
                j = m - 1
            else:
                i = m + 1

        return False
