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
        while head:
            print(str(head.val),end=",")
            head = head.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        
        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next,list2)
        return list1

ln = ListNode()
list1 = ln.create_linked_list([1,3])
list2 = ln.create_linked_list([2])

sol = Solution()
print(ln.print_linked_list(sol.mergeTwoLists(list1,list2)))