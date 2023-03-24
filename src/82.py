class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-101)
        dummy.next, prev, curr = head, dummy, head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next, curr = curr.next, curr.next
            else:
                prev, curr = curr, curr.next

        return dummy.next
