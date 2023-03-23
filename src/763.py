class Solution:
    def partitionLabels(self, s):
        result = []
        head, tail = 0, -1
        tails_dict = { s[i]: i for i in range(len(s)) }

        for i in range(len(s)):
            tail = max(tail, tails_dict[s[i]])

            if(i == tail):
                result.append(tail - head + 1)
                head = tail + 1

        return result
