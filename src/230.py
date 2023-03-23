class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if k == 1:
                return curr.val

            k -= 1
            curr = curr.right
