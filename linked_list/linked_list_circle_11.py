
# 142. Linked List Cycle II

# Companies
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. 
# Note that pos is not passed as a parameter.


# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        else:
            fast = head
            slow = head

            has_cycle = False
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    has_cycle = True
                    break
            if has_cycle == False:
                return None

            slow = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            
            return slow
# Alternative Approach using Hash Set
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head

        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next

        return None
    
# Alternative Approach using Hash Map
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        current = head

        while current:
            if current in visited:
                return current
            visited[current] = True
            current = current.next

        return None

# Floyd’s Tortoise and Hare (Cycle Detection) to find the starting node of the cycle
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head
        has_cycle = False

        # Step 1: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # Step 2: Find the starting node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
