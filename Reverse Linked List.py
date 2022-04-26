class Solution(object):
    def rec(self, prev, now):
        if now is None:
            return prev
        next = now.next
        now.next = prev
        return self.rec(now, next)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        next = head.next
        head.next = None

        return self.rec(head, next)