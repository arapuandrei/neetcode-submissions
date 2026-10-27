"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        cur = head
        newhead=None
        new = None
        map= {}
        while cur:
            if not new:
                new = Node(cur.val)
                newhead=new
            else:
                new.next=Node(cur.val)
                new=new.next
            map[cur]=[new,cur.next,cur.random]
            cur= cur.next
        cur = newhead
        #print(map)
        while cur:
            #print("head",head)
            #print("maphead",map[head])
            #print("map2head",map[head][2])
            if map[head][2] is None:
                #print("none")
                cur.random=None
            else:
                cur.random = map[map[head][2]][0]
            #print("curval",cur.val)
            head=head.next
            cur=cur.next

        
        
        return newhead
            