# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        ptr = newList

        while(list1 != None and list2 != None):
            if(list1.val <= list2.val):
                newList.next = list1
                list1 = list1.next
                newList = newList.next
            else:
                newList.next = list2
                list2 = list2.next
                newList = newList.next

        if(list1 == None and list2):
            newList.next = list2
            list2 = list2.next
        elif(list2 == None and list1):
            newList.next = list1
            list1 = list1.next

        return ptr.next

        