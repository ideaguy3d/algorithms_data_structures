from typing import Optional


# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution1:
    @staticmethod
    def middleNode(head: Optional[ListNode], n) -> Optional[ListNode]:
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head

nodes = ListNode(5)
print(Solution1.middleNode(nodes, 2))



#
