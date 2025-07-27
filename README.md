# 🌳 Tree Practice in Python

Welcome to the **Tree Practice** repository! This collection contains Python implementations of fundamental tree data structure problems, commonly asked in technical interviews and essential for understanding hierarchical data structures.

## 📚 What are Trees?

Trees are hierarchical data structures consisting of nodes connected by edges. Each tree has:
- A **root node** at the top
- **Parent-child relationships** between nodes
- **Leaf nodes** with no children
- Various traversal methods to visit nodes

This repository focuses on **Binary Trees**, where each node has at most two children (left and right).

---

## 📁 Repository Structure

| Filename | Description | Difficulty | LeetCode |
|----------|-------------|------------|----------|
| `balancedBinaryTree.py` | Check if a binary tree is height-balanced | Easy | [LC #110](https://leetcode.com/problems/balanced-binary-tree/) |
| `diameterOfBinaryTree.py` | Find the diameter (longest path) of a binary tree | Easy | [LC #543](https://leetcode.com/problems/diameter-of-binary-tree/) |
| `goodNodes.py` | Count nodes where value >= all ancestor values | Medium | [LC #1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) |
| `inorder.py` | In-order traversal (Left-Root-Right) recursively | Easy | [LC #94](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| `inorder_iterative.py` | In-order traversal using iteration | Easy | [LC #94](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| `invertBinaryTree.py` | Mirror/invert a binary tree | Easy | [LC #226](https://leetcode.com/problems/invert-binary-tree/) |
| `isSubtree.py` | Check if one tree is a subtree of another | Easy | [LC #572](https://leetcode.com/problems/subtree-of-another-tree/) |
| `levelOrderTravesal.py` | Level-order (BFS) traversal of a tree | Medium | [LC #102](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| `maxDepth.py` | Find the maximum depth of a binary tree | Easy | [LC #104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| `postorder.py` | Post-order traversal (Left-Right-Root) | Easy | [LC #145](https://leetcode.com/problems/binary-tree-postorder-traversal/) |
| `preorder.py` | Pre-order traversal (Root-Left-Right) | Easy | [LC #144](https://leetcode.com/problems/binary-tree-preorder-traversal/) |
| `preorder_iterative.py` | Pre-order traversal using iteration | Easy | [LC #144](https://leetcode.com/problems/binary-tree-preorder-traversal/) |
| `rightSideView.py` | View of tree from the right side | Medium | [LC #199](https://leetcode.com/problems/binary-tree-right-side-view/) |
| `sameTree.py` | Check if two trees are identical | Easy | [LC #100](https://leetcode.com/problems/same-tree/) |

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.6 or higher
- Basic understanding of recursion and data structures

### 1. Clone the Repository

```bash
git clone https://github.com/hureramujeeb60/Tree-Practice.git
cd Tree-Practice
```

### 2. Run Individual Solutions

Each file can be run independently:

```bash
python balancedBinaryTree.py
python levelOrderTravesal.py
python maxDepth.py
```

---

## 🎯 Problem Categories

### 🔄 Tree Traversals
- **In-order**: Left → Root → Right (BST gives sorted order)
- **Pre-order**: Root → Left → Right (useful for copying trees)
- **Post-order**: Left → Right → Root (useful for deletion)
- **Level-order**: Level by level (BFS approach)

### 📏 Tree Properties
- **Max Depth**: Height of the tree
- **Balanced Tree**: Height difference ≤ 1 for all subtrees
- **Diameter**: Longest path between any two nodes

### 🔀 Tree Modifications
- **Invert Tree**: Mirror image of the tree
- **Same Tree**: Check structural and value equality
- **Subtree**: Verify containment relationship

---

## 💡 Key Concepts & Patterns

### 1. **Tree Node Structure**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 2. **Recursive Template**
```python
def tree_recursion(root):
    # Base case
    if not root:
        return some_value
    
    # Process current node
    process(root.val)
    
    # Recurse on children
    left_result = tree_recursion(root.left)
    right_result = tree_recursion(root.right)
    
    # Combine results
    return combine(left_result, right_result)
```

### 3. **Iterative Traversal (Using Stack)**
```python
def iterative_traversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Add children to stack
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

### 4. **Level-Order Traversal (Using Queue)**
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Traversal (any) | O(n) | O(h) recursive, O(n) iterative |
| Search | O(n) worst, O(log n) balanced BST | O(h) |
| Insert/Delete | O(n) worst, O(log n) balanced BST | O(h) |
| Height/Depth | O(n) | O(h) |
| Level-Order | O(n) | O(w) where w = max width |

*n = number of nodes, h = height of tree*

---

## 🧪 Testing

Each solution includes test cases in the `__main__` block:

```python
if __name__ == "__main__":
    # Create test tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    # Test solution
    sol = Solution()
    result = sol.method_name(root)
    print(f"Result: {result}")
```

---

## 📈 Learning Path

1. **Start with Traversals**: Master all traversal methods
2. **Tree Properties**: Understand depth, height, balance
3. **Modifications**: Practice inverting and comparing trees
4. **Advanced Problems**: Tackle diameter, good nodes, views
5. **Optimize**: Convert recursive solutions to iterative

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-problem`)
3. Commit your changes (`git commit -m 'Add new tree problem'`)
4. Push to the branch (`git push origin feature/new-problem`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide
- Include problem description and examples
- Add time/space complexity analysis
- Provide comprehensive test cases

---

## 📚 Resources

- [Binary Tree Visualizer](https://www.cs.usfca.edu/~galles/visualization/BST.html)
- [LeetCode Tree Problems](https://leetcode.com/tag/tree/)
- [GeeksforGeeks - Tree Data Structure](https://www.geeksforgeeks.org/binary-tree-data-structure/)
- [Tree Traversal Animations](https://visualgo.net/en/bst)

---

## 👤 Author

**Hurera Mujeeb**

- GitHub: [@hureramujeeb60](https://github.com/hureramujeeb60)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/hureramujeeb/)

---

⭐ If you find this repository helpful, please give it a star!

🔔 Watch this repository to stay updated with new problems and solutions!
