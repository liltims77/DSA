
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that 
# can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that 
# tail's next pointer is connected to. Note that pos is not passed 
# as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.




# SOLUTION APPROACH: Floyd’s Tortoise and Hare (Cycle Detection)
# USE THE NODES INSTEAD OF VALUES TO DETECT CYCLE. Values CAN BE DUPLICATED IN THE LINKED LIST.

# USE HASHMAP OR SET TO STORE THE NODES ALREADY VISITED. IF A NODE IS VISITED AGAIN, THEN THERE IS A CYCLE.

# 🧠 Core Idea: What is a Hash Map?
# A hash map (or hash table) is a data structure that stores data in key-value pairs.

# In Python, a dictionary (dict) is an implementation of a hash map.
# And a set (set) is like a hash map without values (it only stores unique keys).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
# # Alternative Approach using Hash Set
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False

# # Alternative Approach using Hash Map
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        current = head

        while current:
            if current in visited:
                return True
            visited[current] = True
            current = current.next

        return False