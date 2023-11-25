'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has 
Node.val == val, and return the new head.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:


        dummy_head = ListNode(next=head)
        current = dummy_head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next