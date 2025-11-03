


# from pathlib import Path

# # Create a Python file containing all the DSA approach notes
# content = """\
# # DSA Problem Solving Guide
# # Author: ChatGPT (for Timilehin)
# # Purpose: Step-by-step structured approach for solving DSA questions

# """
# content += r'''
# """
# 💡 STEP 1: Understand the Problem
# ---------------------------------
# - Read carefully; don’t rush to code.
# - Restate the problem in your own words.
# - Identify inputs, outputs, and constraints.
# - Study the examples — especially edge cases.
# """

# """
# 💡 STEP 2: Identify the Data Structure
# --------------------------------------
# Recognize the main data structure involved:

# - Arrays / Strings → sliding window, two pointers, hashing
# - Linked List → pointers, reverse, merge, detect cycle
# - Stack / Queue → parentheses, next greater element, BFS
# - Tree / Graph → DFS, BFS, recursion
# - Heap / Priority Queue → top K, shortest path
# - Hash Map / Set → frequency count, duplicates
# """

# """
# 💡 STEP 3: Recognize the Pattern
# --------------------------------
# Common patterns and their example use cases:

# | Pattern             | Example Problem              | Typical Approach                   |
# |---------------------|------------------------------|------------------------------------|
# | Two Pointers        | Sorted array sum             | Start at ends, move inward         |
# | Sliding Window      | Longest substring            | Expand & shrink window             |
# | Fast/Slow Pointers  | Linked list cycle detection  | Move one fast, one slow            |
# | Recursion / DFS     | Tree traversals              | Call function recursively          |
# | BFS / Queue         | Shortest path                | Use queue layer by layer           |
# | Backtracking        | Permutations, subsets        | Try → Recurse → Undo               |
# | Dynamic Programming | Fibonacci, knapsack          | Break into subproblems             |
# | Sorting + Greedy    | Intervals, meeting rooms     | Sort, then decide locally          |
# | Hash Map Counting   | Subarray sum equals K        | Store prefix sums                  |
# """

# """
# 💡 STEP 4: Write Pseudocode
# ---------------------------
# Before coding, outline your logic in plain words:
# Example:
#     Loop through array
#     For each number, check if (target - num) exists in map
#     If yes, return both indices
# """

# """
# 💡 STEP 5: Optimize (If Needed)
# -------------------------------
# - Can it run faster? (Use hash maps, two pointers, etc.)
# - Can it use less memory? (Modify in-place, reuse structures)
# Even if not optimal, mention your improvement ideas.
# """

# """
# 💡 STEP 6: Write Clean Code
# ---------------------------
# - Use descriptive variable names
# - Keep loops & conditions simple
# - Comment key steps
# Example: Reverse Linked List
# """

# # Example code block
# content += """\
# def reverseList(head):
#     prev = None
#     curr = head

#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp
#     return prev
# """

# content += r'''
# """
# 💡 STEP 7: Test with Examples
# -----------------------------
# Always test with:
# - Provided examples
# - Edge cases (empty, single element, duplicates, etc.)
# Print intermediate variables to debug.
# """

# """
# 💡 STEP 8: Reflect After Each Question
# --------------------------------------
# - What pattern did I just use?
# - What mistake slowed me down?
# - What can I do differently next time?
# """

# """
# 🧭 SUMMARY CHECKLIST
# --------------------
# ✅ Understand problem & constraints
# ✅ Identify data structure
# ✅ Recognize pattern
# ✅ Write pseudocode
# ✅ Implement cleanly
# ✅ Test thoroughly
# ✅ Reflect & learn
# """

# """
# 💪 Final Words
# --------------
# DSA is not about memorizing code.
# It’s about structured problem-solving and logical flow.
# Once you master this thinking pattern, you can solve any problem confidently.
# """
# '''

# path = Path("/mnt/data/DSA_Problem_Solving_Guide.py")
# path.write_text(content)

# path
