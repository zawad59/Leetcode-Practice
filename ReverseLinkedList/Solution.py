class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while(current!=None):
            current = current.next
            head.next = prev
            prev = head
            head = current
        return prev

        
