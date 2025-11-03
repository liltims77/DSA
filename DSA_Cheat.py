

# Arrays / Lists

# Iterate through list
for num in nums:  
    ...

# Iterate with index
for i in range(len(nums)):  
    ...

# Reverse iteration
for i in range(len(nums)-1, -1, -1):  
    ...

# Two pointers (start + end)
left, right = 0, len(nums)-1
while left < right:
    ...
    left += 1
    right -= 1

# Sliding window
window_sum = 0
left = 0
for right in range(len(nums)):
    window_sum += nums[right]
    while window_sum > target:  # shrink window
        window_sum -= nums[left]
        left += 1


#####################################################################################################################################
# Strings

# Reverse a string
s[::-1]

# Palindrome check
s == s[::-1]

# Frequency count
from collections import Counter
Counter(s)

# Remove spaces/punctuation
import re
clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

################################################################################################################
# 🔹 Linked List

# Traverse
node = head
while node:
    print(node.val)
    node = node.next

# Detect cycle (Floyd’s)
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False

# Reverse linked list
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev



##################################################################################################################################################

# 🔹 Hash Map / Set

# Check duplicates
seen = set()
for x in nums:
    if x in seen: return True
    seen.add(x)

# Frequency count
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1



###########################################################################################################################################

# Binary Search

left, right = 0, len(nums)-1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1


###########################################################################################################################################

# 🔹 Recursion / DFS

def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)


####################################################################################################################

# 🔹 Dynamic Programming

# Fibonacci
dp = [0, 1]
for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])

##################################################################################################
# 🔹 Sorting

nums.sort()              # in-place
sorted_nums = sorted(nums)  # new list

##########################################################################################################

# ✅ Beginner tip:
# If it’s an array/list problem → think for or while with indexes, or sliding window.
# If it’s a linked list problem → think while node: or two pointers.
# If it’s a search problem → think binary search.
# If it’s a path/tree/graph problem → think DFS/BFS (recursion or queue).



#######################################################################################################################################

# 🔑 General Rules
# 1. Use List (Array) when:
# You care about order (index matters).
# You need to iterate over elements in sequence.
# You may need to store duplicates.
# Common operations:
# Appending values
# Iterating in order
# Accessing by index
# ✅ Example problems:
# Rotate an array
# Find max/min in a list
# Two-pointer problems (like 3Sum, 2Sum sorted)


# 2. Use Set when:
# You care about uniqueness (no duplicates).
# You need fast membership check (x in myset) → O(1).
# You don’t care about the order of elements.
# Common operations:
# Checking if something exists
# Removing duplicates
# Set operations (union, intersection, difference)
# ✅ Example problems:
# “Find if array has duplicates” → len(nums) != len(set(nums))
# “Find missing number in range” → compare set of expected vs actual
# “Check if two words are anagrams” → compare set(word1) and set(word2)


# 3. Use Dict (HashMap) when:
# You need to map keys to values.
# You want counting/frequency of items.
# You need fast lookup with extra info about an element.
# Common operations:
# Store counts → Counter or manual {num: count}
# Store seen values with their index
# Grouping items by some property
# ✅ Example problems:
# Two Sum (store num → index)
# Count characters in a string
# Group words by anagram pattern
# ⚡ Quick Cheat Sheet
# Problem Type	Likely DS
# Ordered list of items, duplicates allowed	List
# Need fast existence check, no duplicates	Set
# Need to count things / map key→value	Dict




# | Feature               | **For Loop**                                   | **While Loop**                                                        |
# | --------------------- | ---------------------------------------------- | --------------------------------------------------------------------- |
# | **Use when**          | You *know* the number of iterations beforehand | You *don’t know* how many times to loop — depends on a **condition**  |
# | **Common use cases**  | Arrays, lists, counting, fixed ranges          | Searching until a condition is met, pointer movement, reading streams |
# | **Typical structure** | `for i in range(n):`                           | `while condition:`                                                    |
# | **Best for**          | Iterating a fixed number of times              | Iterating *until* something happens                                   |


# 💡 Rule of Thumb

# Use for when you know how many times.
# Use while when you don’t.