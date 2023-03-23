class Solution:
    def trap(self, height):
        stack, r = [], 0

        for i in range(len(height)):
            m = 0

            while stack:
                h, j = stack[-1]

                if h <= height[i]:
                    stack.pop()
                    r += (h - m) * (i - j)
                    m = h
                else:
                    r += (height[i] - m) * (i - j)
                    break

            stack.append((height[i], i))

        return r
