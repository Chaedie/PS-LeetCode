# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenOfLinkedList = 0
        pointer = head
        while pointer:
            lenOfLinkedList += 1
            pointer = pointer.next
            
        midPointer = lenOfLinkedList // 2
            
        for _ in range(midPointer):
            head = head.next
        return head