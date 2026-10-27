# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverselk(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next   # save next
            current.next = prev        # reverse pointer
            prev = current             # move prev
            current = next_node        # move current
        return prev

    def lenlk(self,head):
        n = 0
        tmphead = head
        while tmphead:
            #print(tmphead.val,"->")
            tmphead=tmphead.next
            n+=1
        return n

    def splitIn2(self,head):
        n = self.lenlk(head)
        tmphead=head
        for i in range(0,n//2-1):
            tmphead=tmphead.next
        return tmphead

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.splitIn2(head)
        tmp = mid.next
        mid.next = None
        mid = tmp
        midc=mid
        mid = self.reverselk(mid)
        headc = head
        #print(self.lenlk(head))
        #print(self.lenlk(mid))
        lmid =None
        while mid and headc:
            #print(self.lenlk(headc))
            #print(self.lenlk(mid))
            tmp = headc.next
            headc.next = mid
            lmid=mid
            tmpm = mid.next
            mid.next = tmp
            headc=tmp
            mid=tmpm
        #print(type(mid))
        #print(type(headc))
        #print(type(tmp))
        if lmid is not None:
            lmid.next=mid
        #print(self.splitIn2(head))