# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr = None, head

        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev
        # THis solution is iterative. 3pointers used. very fundamental prblem for future linkedlist probs. 
        # T: O(n) M"O(1)

        #there's onemore solution to it that recursive. kind of confusing. 
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 

        return prev