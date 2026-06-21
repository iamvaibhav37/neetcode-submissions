# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes= []
        curr = head 
# this is the brute force space O(n) soln. using list. 
        while curr:
            nodes.append(curr)
            curr =curr.next
        
        k = len(nodes) - n
        if k == 0:
            return head.next

        if k+1 < len(nodes):
            nodes[k-1].next = nodes[k+1]
        else:
            nodes[k-1].next = None
        return head

        

