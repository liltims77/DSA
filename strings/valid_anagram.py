
# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # using HASH map -->> uses extra memory

        if len(s) != len(t):
            return False
        
        # creating Hash Maps
        countS = {}
        countT = {}

        for i in range(len(s)):
        # we use len(s) because they are of thesame length we use index i for both of the strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # countS[s[i]] = 1 + countS[s[i]]
            # key of hash map s we increament it by 1
            # if the character doesnt exist in the hash map yet, it will throw key error, thats why we use 
            # countS[s[i]] = 1 + countSget(s[i], 0) if key does not exist, it will return default value 0

            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True



# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         # using HASH map -->> uses extra memory
#         return Counter(s) == Counter(t)
    


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         # 0(1) -->> NO extra memory
#         # Using sorting algorithm doesnt take extra space

#         return sorted(s) == sorted(t)









        






        


        