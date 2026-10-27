# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        slow = head
        fast = None
        while slow!=fast:
            if fast == None:
                fast = slow
            if slow.next != None and fast.next!=None and fast.next.next !=None:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return True