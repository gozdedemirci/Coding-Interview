- Array: 
    - A collection of elements of the same type, stored in contiguous memory locations.
- Linked List: 
    - A linear data structure where each element (node) contains a reference to the next node.
- Stack: 
    - A data structure that follows the Last-In-First-Out (LIFO) principle.
- Queue: 
    - A data structure that follows the First-In-First-Out (FIFO) principle.
- Tree: 
    - A hierarchical data structure with a set of connected nodes, where each node can have zero or more child nodes.
- Graph: 
    - A non-linear data structure consisting of a set of vertices (nodes) and edges that connect them.
- Hash Table: 
    - A data structure that maps keys to values using a hash function.
- Heap: 
    - A complete binary tree-based data structure that satisfies the heap property. Two main types of heaps are min-heap and max-heap.
        - Min-heap: 
            - The value of each node is **less than or equal** to the value of its parent, with the minimum-value element at the root.
        - Max-heap:
            - The value of each node is **greater than or equal** to the value of its parent, with the maximum-value element at the root.
    - ***Priority Queue:***
        - A queue where each element has a priority associated with it. Elements with higher priorities are served before elements with lower priorities.
- Trie: 
    - A tree-like data structure used to store a collection of strings efficiently.
- Set: 
    - A collection of unique elements with no particular order.
- Map: 
    - A collection of key-value pairs, where each key is unique.



**Time Complexity**:

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

|-------------------------------------------------------------|
|           Time Complexity with Worst Case Scenario          |
|-------------------------------------------------------------|
| Data Structure | Access   | Search   | Insertion | Deletion |
|----------------|----------|----------|-----------|----------|
| Array          | O(1)     | O(n)     | O(n)      | O(n)     |
| Linked List    | O(n)     | O(n)     | O(1)      | O(1)     |
| Stack          | O(n)     | O(n)     | O(1)      | O(1)     |
| Queue          | O(n)     | O(n)     | O(1)      | O(1)     |
| Tree           | O(log n) | O(log n) | O(log n)  | O(log n) |
| Graph          | O(V+E)   | O(V+E)   | O(1)      | O(1)     |
| Hash Table     | N/A      | O(1)     | O(1)      | O(1)     |
| Heap           | O(1)     | O(log n) | O(log n)  | O(log n) |
| Priority Queue | O(1)     | O(log n) | O(log n)  | O(log n) |
| Trie           | O(m)     | O(m)     | O(m)      | O(m)     |
|-------------------------------------------------------------|

### **Notes**:
    - V: Number of vertices
    - E: Number of edges
    - n: Number of elements in the data structure
    - m: Length of the key

