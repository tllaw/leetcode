class Solution:
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                el = "FizzBuzz"
            elif i % 3 == 0:
                el = "Fizz"
            elif i % 5 == 0:
                el = "Buzz"
            else:
                el = str(i)

            result.append(el)

        return result
