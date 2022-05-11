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
    
        #Leetcode solution 2 
        
        # Fast is going faster twice of slow
        # if fast is reach end of the linkedList
        # then slow is reach mid of the linkedList
        
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow