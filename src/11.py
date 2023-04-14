class Solution:
    def maxArea(self, height):
        i, j, r = 0, len(height) - 1, -1

        while i < j:
            r = max(r, (j - i) * min(height[i], height[j]))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return r
