# 🧠 Linked Lists in Python — Complete Beginner Guide

A **Linked List** is a data structure used to store a collection of elements (called **nodes**), where each node contains:
1. **Data** – the value of the element.
2. **Next** – a reference (or pointer) to the next node in the list.

Unlike Python lists, linked lists **don’t store data in continuous memory**.  
Each element is connected through links (pointers), forming a chain-like structure.

---

## 🔗 Example Visualization

```
[10 | next] → [20 | next] → [30 | next] → None
```

- `10`, `20`, `30` are data values.
- Each node points to the next.
- The last node points to `None`, marking the end of the list.

---

## 🧱 Step 1: Create a Node Class

Every node will have:
- `data`: to store the element's value
- `next`: to store a reference to the next node

```python
class Node:
    def __init__(self, data):
        self.data = data      # stores the data
        self.next = None      # initially points to nothing
```

### Example usage:
```python
node1 = Node(10)
node2 = Node(20)
node1.next = node2

print(node1.data)       # Output: 10
print(node1.next.data)  # Output: 20
```

---

## 🧩 Step 2: Create a LinkedList Class

The LinkedList class will keep track of the **head node** and provide helper methods to add, print, and delete nodes.

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

---

## ➕ Step 3: Append Nodes to the Linked List

This function will add new nodes at the **end** of the list.

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        # Add the new node at the end
        current.next = new_node
```

---

## 🖨️ Step 4: Print All Nodes in the List

```python
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

---

## 🧪 Step 5: Test the Linked List

```python
# Full working example

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Create LinkedList and add nodes
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

# Print the list
ll.print_list()
```

### ✅ Output:
```
10
20
30
```

---

## 🧠 Summary

| Concept | Description |
|----------|--------------|
| **Node** | Represents a single element with data and a pointer to the next node. |
| **Head** | The first node in the linked list. |
| **Next** | Reference to the next node in the list. |
| **Append()** | Adds a new node at the end. |
| **Print()** | Traverses and displays all node values. |

---

## 📘 Key Takeaways

- Linked lists store elements **non-contiguously** in memory.
- Each node knows only about the **next** node.
- Inserting or deleting at the start is faster than in arrays.
- Traversal is **O(n)** because you must move node by node.

---

👨‍💻 **Author:** Timilehin’s Linked List Learning Notes  
📅 **Topic:** Data Structures in Python  
📂 **File:** `linked_list_in_python.md`
