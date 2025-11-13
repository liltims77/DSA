

# 2487. Remove Nodes From Linked List

# Hint
# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to 
# the right side of it.

# Return the head of the modified linked list.

 

# Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.


# Example 2:
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
 

# Constraints:

# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        # Reverse the linked list
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Now prev is the new head of the reversed list
        new_head = prev
        
        # Traverse the reversed list and remove nodes
        max_val = float('-inf')
        dummy = ListNode(0)
        dummy.next = new_head
        current = dummy
        
        while current.next:
            if current.next.val >= max_val:
                max_val = current.next.val
                current = current.next
            else:
                current.next = current.next.next
        
        # Reverse the list again to restore original order
        prev = None
        current = dummy.next
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev