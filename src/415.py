class Solution:
    def addStrings(self, num1, num2):
        num1, num2, c, result = list(num1), list(num2), 0, []

        while num1 or num2 or c:
            n1 = ord(num1.pop()) - ord("0") if num1 else 0
            n2 = ord(num2.pop()) - ord("0") if num2 else 0
            result.append(str((n1 + n2 + c) % 10))
            c = (n1 + n2 + c) // 10

        result = "".join(result[::-1])
        return result
