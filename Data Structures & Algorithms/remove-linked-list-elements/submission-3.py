# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        if head == None:
            return None
        headc = head
        while headc:
            if headc.next:
                tmp = headc.next
                #print(tmp.val)
                while tmp.val==val:
                    tmp=tmp.next
                    if tmp == None:
                        break
                headc.next = tmp
            headc=headc.next
        return head


