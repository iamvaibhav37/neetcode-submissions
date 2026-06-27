# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)  #this add direct Listnode in the nodes arr, not as an int. if want int, do curr.val
            curr =curr.next
#u solved on your own, this is O(n) space solution. TC is O(n) no other way. 
#try solving i O(1) space. 
        segs = [] 
        for i in range(0, len(nodes), k):
            segs.append(nodes[i:i+k])

        for lst in segs:
            if len(lst) == k:
                lst.reverse()

        dummy = ListNode()
        tail = dummy    
        for lst in segs:
            for node in lst:
                tail.next = node
                tail = tail.next
        tail.next = None

        return dummy.next

            
        
