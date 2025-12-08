
# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:
# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:



# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next: # because we have 2 nodes to reverse, not just 1 node
            # save pointers/node
            nxtPair = curr.next.next
            second = curr.next # give second node pointer a variable

            # reverse the paris
            second.next = curr
            curr.next = nxtPair 
            prev.next = second # second node put in first position

            # update pointers
            prev = curr
            curr = tmp

        return dummy.next

        