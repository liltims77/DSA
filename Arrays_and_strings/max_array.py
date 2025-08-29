# 📝 Sample Question 1:

# Find the maximum number in an array.

# 👉 Example:
# Input: [3, 7, 1, 9, 2]
# Output: 9



def find_max(arr):


    max_num = arr[0] # Assume the first element is the maximum

    for num in arr: 

        if num > max_num:
            max_num = num

    return max_num

# Example usage
numbers = [3, 7, 1, 9, 2]
print(find_max(numbers))  # Output: 9



# If we run it step by step with numbers = [3, 7, 1, 9, 2]:

# Start max_num = 3

# Compare 3 with 3 → not bigger → else: print message.

# Compare 7 with 3 → bigger → update max to 7.

# Compare 1 with 7 → not bigger → else runs.

# Compare 9 with 7 → bigger → update max to 9.

# Compare 2 with 9 → not bigger → else runs.

# Final result = 9.




# Why no else block?
# Because we don’t need to do anything when the condition num > max_num is false.
# The job of this loop is: keep track of the biggest number so far.
# If the current number num is bigger → we update max_num.
# If not → we just move on (no action needed).





# What would happen if we added an else?
for num in arr:
    if num > max_num:
        max_num = num
    else:
        pass   # nothing to do here


# When would an else be useful?
# If you had two different actions depending on the comparison. For example:

for num in arr:
    if num > max_num:
        max_num = num
    else:
        print(num, "is not bigger than current max")
# Here the else is meaningful, because it runs some code when the condition is false.
# But in your find_max function, there’s no alternative action required—so the else was simply left out. ✅






