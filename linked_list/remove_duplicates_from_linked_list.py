
# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr is not None:
            while curr.next and curr.next.val == curr.val: #This handles deleting the node. we need to make sure the next node exists ie doing curr.next[while curr.next]
              curr.next = curr.next.next  # this deletes the curr.next node and assigns curr.next to the node after curr.next
            curr = curr.next # move curr forward after  deletion and iteration
        return head

        