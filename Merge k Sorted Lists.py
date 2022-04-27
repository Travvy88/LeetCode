class ListNode:
   def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def rec(heads, ):
            idx = -1
            mn = inf
            flag = True
            for i, head in enumerate(heads):
                if head is not None:
                    flag = False
                    val = head.val
                    if val < mn:
                        mn = val
                        idx = i

            if flag:
                return
            result.append(mn)
            heads[idx] = heads[idx].next
            rec(heads, )

        result = []
        rec(lists, )
        prev = None
        if len(result) == 0:
            return None
        else:
            for i in range(len(result) - 1, -1, -1):
                last = ListNode(result[i], prev)
                prev = last

            return last
