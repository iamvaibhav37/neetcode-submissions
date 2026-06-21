# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes= []
        curr = head 

        while curr:
            nodes.append(curr)
            curr =curr.next
        
        k = len(nodes) - n
        if k == 0:
            return head.next

        nodes[k-1].next = nodes[k+1] if k+1 < len(nodes) else None
        return head

        

