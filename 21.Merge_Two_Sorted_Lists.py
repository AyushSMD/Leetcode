# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_linked_list(values):
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

        return head
    
    @staticmethod
    def print_linked_list(head):
        values = []
        while head:
            print (str(head.val),end=",")
            head = head.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else :
                list1.val > list2.val
                current.next = list2
                list2 = list2.next
                current = current.next

        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next

ln = ListNode()
list1 = ln.create_linked_list([])
list2 = ln.create_linked_list([0])

sol = Solution()
ln.print_linked_list(sol.mergeTwoLists(list1,list2))
