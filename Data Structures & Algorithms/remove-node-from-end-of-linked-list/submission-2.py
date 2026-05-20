# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        total = 0

        # find length
        while curr:
            total+=1
            curr = curr.next

        if n == total:
            return head.next
        
        count = 0
        curr = head
        prev = None
        while curr:
            count+=1
            if count == (total - n +1):
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next 
        return head

