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

<table>
  <tr>
    <th colspan="5"> Time Complexity with Worst Case Scenario</th>
  </tr>
  <tr>
    <th>Data Structure</th>
    <th>Access</th>
    <th>Search</th>
    <th>Insertion</th>
    <th>Deletion</th>
      
  </tr>
  <tr>
    <td>Array</td>
    <td>O(1)</td>
    <td>O(n)</td>
    <td>O(n)</td>
    <td>O(n)</td>
  </tr>
  <tr>
   <td>Linked List</td>
    <td>O(n)</td>
    <td>O(n)</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Stack</td>
    <td>O(n)</td>
    <td>O(n)</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Queue</td>
    <td>O(n)</td>
    <td>O(n)</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Tree</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
  </tr>
  <tr>
    <td>Graph</td>
    <td>O(V+E)</td>
    <td>O(V+E)</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Hash Table</td>
    <td>N/A</td>
    <td>O(1)</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Heap</td>
    <td>O(1)</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
  </tr>
  <tr>
    <td>Priority </td>
    <td>O(1)</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
    <td>O(log n)</td>
  </tr>
 <tr>
    <td>Trie</td>
    <td>O(m)</td>
    <td>O(m)</td>
    <td>O(m)</td>
    <td>O(m)</td>
  </tr>
</table>


### **Notes**:
    - V: Number of vertices
    - E: Number of edges
    - n: Number of elements in the data structure
    - m: Length of the key

