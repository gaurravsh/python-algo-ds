# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        
        head2=head
        while head2.next is not None:
            head = head.next
            head2 = head2.next
            if head2.next is not None:
                head2 = head2.next
                
        return head