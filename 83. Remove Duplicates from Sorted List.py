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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        por = head
        current = head.next

        while current:
            if por.val < current.val:
                por.next=current
                por = current
            elif por.val == current.val:
                por.next=current.next
                
            current = current.next

        # while current:
        #     if current.next:
        #         if current.val < current.next.val:
        #             # print (current.val)
        #             current.next = current.next.next
        #     current = current.next



        return head

ln = ListNode()
list = ln.create_linked_list([])

sol = Solution()
print(ln.print_linked_list(sol.deleteDuplicates(list)))