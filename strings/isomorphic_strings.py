# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

 

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true



s = "egg"
t = "add"

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
        # zip(s, t) pairs characters from s and t one-by-one. For s="egg" and t="add", zip gives pairs: ('e','a'), ('g','d'), ('g','d')
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True


sol = Solution()
print(sol.isIsomorphic("egg", "add"))  # True