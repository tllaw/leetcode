class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = [n - 1]
        result = [0] * n

        for i in range(n - 2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            result[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return result
