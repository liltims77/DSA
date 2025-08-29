# ✅ O(log n) – Logarithmic Time

# You cut the problem in half each time → very fast growth.
# Typical in binary search.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([1, 2, 4, 8], 10))


# 👉 Output: -1

# Your array: [1, 2, 4, 8]
# Target: 10
# Steps:
# left = 0, right = 3
# mid = (0 + 3) // 2 = 1 → arr[1] = 2
# Since 2 < 10, move left → mid + 1 = 2.
# left = 2, right = 3
# mid = (2 + 3) // 2 = 2 → arr[2] = 4
# Since 4 < 10, move left → mid + 1 = 3.
# left = 3, right = 3
# mid = (3 + 3) // 2 = 3 → arr[3] = 8
# Since 8 < 10, move left → mid + 1 = 4.
# Now left = 4, right = 3 → loop ends.
# 🔹 Target 10 is not in the array, so the function returns -1.

# | Step | `left` | `right` | `mid = (left+right)//2` | `arr[mid]` | Comparison with target (10) | Action                    |
# | ---- | ------ | ------- | ----------------------- | ---------- | --------------------------- | ------------------------- |
# | 1    | 0      | 3       | 1                       | 2          | `2 < 10`                    | Move `left` → `mid+1 = 2` |
# | 2    | 2      | 3       | 2                       | 4          | `4 < 10`                    | Move `left` → `mid+1 = 3` |
# | 3    | 3      | 3       | 3                       | 8          | `8 < 10`                    | Move `left` → `mid+1 = 4` |
# | 4    | 4      | 3       | —                       | —          | `left > right`              | Loop ends → return `-1`   |


print(binary_search([1, 2, 4, 8], 4))
# 👉 Final Result: 2 (the index of 4 in the array).
# | Step | `left` | `right` | `mid` | `arr[mid]` | Comparison with target (4) | Action             |
# | ---- | ------ | ------- | ----- | ---------- | -------------------------- | ------------------ |
# | 1    | 0      | 3       | 1     | 2          | `2 < 4`                    | Move `left` → 2    |
# | 2    | 2      | 3       | 2     | 4          | `4 == 4`                   | Found → return `2` |




def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return -1
    
print(binary_search([1, 2, 4, 8], 10))

# 👉 Final Result: 4 (the index of 10 in the array).
# | Step | `left` | `right` | `mid = (left+right)//2` | `arr[mid]` | Comparison with target (10) | Action                    |
# | ---- | ------ | ------- | ----------------------- | ---------- | --------------------------- | ------------------------- |
# | 1    | 0      | 4       | 2                       | 4          | `4 < 10`                    | Move `left` → `mid+1 = 3` |
# | 2    | 3      | 4       | 3                       | 8          | `8 < 10`                    | Move `left` → `mid+1 = 4` |
# | 3    | 4      | 4       | 4                       | 10         | `10 == 10`                  | Found → return `4`        |



