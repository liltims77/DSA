

# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.









class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using extra memory
        newstr = ""

        for c in s:
            if c.isalnum():
                newstr += c.lower()

        return  newstr == newstr[::-1]
    
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        return s == s[::-1]



class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer forward if not alphanumeric
            if not s[left].isalnum():
                left += 1
                continue

            # Move right pointer backward if not alphanumeric
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare both characters (ignore case)
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers toward the center
            left += 1
            right -= 1

        return True



  



        