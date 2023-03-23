class Solution:
    def mergeTwoLists(self, p, q):
        # return self.recursion(p, q)
        return self.iteration(p, q)

    def recursion(self, p, q):
        if not p or not q:
            return p if p else q

        p, q = (p, q) if p.val < q.val else (q, p)
        p.next = self.mergeTwoLists(p.next, q)
        return p

    def iteration(self, p, q):
        curr = head = ListNode()

        while p and q:
            p, q = (p, q) if p.val < q.val else (q, p)
            curr.next = p
            curr, p = curr.next, p.next

        if p or q:
            curr.next = p if p else q

        return head.next
