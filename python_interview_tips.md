
import pypandoc

cheat_sheet_md = """
# 🐍 Python Interview Cheat Sheet  

### 1. 🔎 First Step – Understand the Question
- What are the **inputs**?  
- What are the **outputs**?  
- Any **constraints** (size, time, memory)?  

---

### 2. 🛠️ General Problem-Solving Template
1. Restate problem in your own words.  
2. Solve small example by hand.  
3. Start with brute force.  
4. Optimize (think dict, set, sorting, heap).  
5. Test with edge cases.  

---

### 3. 📦 Python Built-ins You Must Use
- **Dict/Set** → fast lookup (`in`, `dict.get()`)  
- **Counter** → frequency counts  
- **Sorted() with key** → custom sorting  
- **Max/Min with key** → find element with condition  
- **Enumerate()** → index + value  
- **Zip()** → pair lists  
- **Heapq** → smallest/largest efficiently  

---

### 4. 🎯 Common Patterns
- **Hash Map** → first unique, two sum, frequency problems  
- **Two Pointers** → sorted arrays, substrings, palindromes  
- **Sliding Window** → max subarray, longest substring  
- **Stack** → valid parentheses, next greater element  
- **Queue / BFS** → shortest path, level order traversal  
- **Recursion / DFS** → trees, graphs, backtracking  
- **Dynamic Programming** → Fibonacci, knapsack, subsequences  

---

### 5. 🧪 Edge Cases to Always Test
- Empty input (`[]`, `""`)  
- One element  
- All same values  
- Negative numbers  
- Large input size  

---

### 6. ⚡ Time Complexity Quick Guide
- List `.append` → O(1)  
- Dict/Set lookup → O(1) avg  
- Sorting → O(n log n)  
- Nested loops → O(n²)  
- BFS/DFS → O(V+E)  

---

### 7. 💡 Code Skeleton (Safe Start)
```python
def solve_problem(input_data):
    # Step 1: Handle edge cases
    if not input_data:
        return None
    
    # Step 2: Brute force idea
    # ...
    
    # Step 3: Optimized solution
    # ...
    
    return result
