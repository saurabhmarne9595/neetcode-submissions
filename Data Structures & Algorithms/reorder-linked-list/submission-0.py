# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow is at mid
        # reverse  list from slow and get it's header
        
        second = slow.next
        slow.next = None
    
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev is head of revered string
        # i'm worried that it's gonna create a cycle
        
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next  
            
            first.next = second
            second.next = tmp1
            
            first = tmp1            
            second = tmp2


        
