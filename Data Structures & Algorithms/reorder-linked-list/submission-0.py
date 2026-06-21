# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
    #finding the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    #assigning the middle point as start of second half of the LL and endpoint of 1st half to None
        second = slow.next
        slow.next = None

    #reversing the second half
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next 
    #Merge both lists. 
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next   #since we are going to break this links, we need to save them first. 
            first.next = second
            second.next = tmp1
            first = tmp1    #assigning/ moving forward the first ptr and second ptr 
            second = tmp2 

        

        