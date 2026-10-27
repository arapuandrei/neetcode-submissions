# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = l1
        carry = 0
        l3 = None
        tmp3 = None
        while l1!= None and l2!=None:
            
            print(l1.val, l2.val, carry)
            if l3 == None:
                l3 = ListNode(int(l1.val + l2.val + carry) % 10)
                tmp3 = l3
            else:
                tmp3.next = ListNode(int(l1.val + l2.val + carry) % 10)
                tmp3 = tmp3.next
            carry = int(l1.val +l2.val + carry) // 10
            print(tmp3.val)
            if l1.next ==None and l2.next!=None:
                l1.next= ListNode(0)
            elif l1.next !=None and l2.next==None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            
        if carry>0:
            tmp3.next = ListNode(carry)
        return l3
        