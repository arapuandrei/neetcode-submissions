# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        cal = 0;
        t = head
        while t !=None:
            t= t.next
            cal += 1
        n=cal-n
        print(n)
        if n < 1:
            return head.next
        for i in range(0, n-1):
            tmp = tmp.next
        if tmp.next:
            tmp.next = tmp.next.next
        else:
            tmp.next = None
        return head