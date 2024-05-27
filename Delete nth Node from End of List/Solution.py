class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        ptr = temp
        dummy = None
        if(head.next==None):
            return head.next
        else:
            x = 1
        while(head!=None):
            head = head.next
            x+=1
        target = x - n
        t = 1
        while(temp!=None):
            if(t == target- 1):
                temp.next = temp.next.next
                return ptr
            elif(t==target):
                temp = temp.next
                #temp = temp.next
                return temp
            temp = temp.next
            t+=1