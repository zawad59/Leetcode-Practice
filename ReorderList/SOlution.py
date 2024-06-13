class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack=[]
        node=head
        while node:
            stack.append(node)
            node=node.next
        node=head
        for i in range(len(stack)//2):
            n = stack.pop()
            link = node.next
            node.next = n
            n.next = link
            node = link
        node.next = None