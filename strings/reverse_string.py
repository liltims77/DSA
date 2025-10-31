
# 344. Reverse String
# Easy

# Write a function that reverses a string. The input string is given as an 
# array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.


##################################################################################################################################

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Time: 0(n) Space 0(1)

        l = 0
        r = len(s) -1

        while l < r:
            s[l], s[r] = s[r], s[l]
            # swapping in python
            l = l + 1
            r = r -1

#########################################################################################################################################

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # using STACK 0(n)

        stack = []

        for c in s:
            stack.append(c)
            # So the top of the stack (the last element) is 'o', and the bottom is 'h'.

        i = 0
        while stack:
            s[i]  = stack.pop()
            i = i + 1


sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))  # ["o","l","l","e","h"]



#######################################################################################################################

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # using RECURSION -> Recursion takes extra spaces
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r -1)
        reverse(0, len(s) -1)

