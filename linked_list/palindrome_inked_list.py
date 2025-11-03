
# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 
# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false
 

# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        # find middle (slow)
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow is not None:
            tmp = slow.next
            slow.next = prev  # We make the current node (slow) point backward (<<---) — to prev.  # So instead of pointing to the next node, it now points to the previous one.
            prev = slow #We move the prev pointer one step forward.  # Now, prev becomes the current node (the one we just reversed).
            slow = tmp  # We move the slow pointer one step forward using the tmp variable we saved earlier.


        # check if palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # putting it inside an aray
        nums = []

        while head is not None:
            nums.append(head.val) # add the values inside the array
            head = head.next # update the pointer

            # arrar algorithm to check if it is a palindrome or not
        l = 0
        r = len(nums) -1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l = l+1
            r = r-1

        return True