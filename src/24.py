class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        curr, next = head.next, head.next.next
        curr.next = head
        head.next = self.swapPairs(next)
        return curr
