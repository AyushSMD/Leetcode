from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_llist(list):
    if list is None:
        return None
    head = ListNode(list[0])
    current = head
    for value in list[1::]:
        current.next=ListNode(value)
        current = current.next
    return head

def print_llist(head):
    current = head
    while current:
        print (current.val, end="->")
        current = current.next
    print()

l1=create_llist([9,9,9,9,9,9,9])
l2=create_llist([9,9,9,9])
print_llist(l1)
print_llist(l2)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None
        
        
        sol = ListNode(0)
        currentSol = sol
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1+val2+carry
            carry = total//10
            currentSol.next=ListNode(total%10)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            currentSol = currentSol.next
        
        if carry:
            currentSol.next=ListNode(carry)

        return sol.next

solObj = Solution()
print_llist(solObj.addTwoNumbers(l1,l2))