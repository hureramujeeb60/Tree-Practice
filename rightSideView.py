from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()
                if i == level_size - 1:
                    res.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
        return res

if __name__ == "__main__":
    # Manually building the binary tree:
    #          1
    #         / \
    #        2   3
    #       / \   \
    #      4   5   6
    #           \
    #            7

    # Level 1 (Root)
    root = TreeNode(1)
    
    # Level 2
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    # Level 3
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    # Level 4
    root.left.right.right = TreeNode(7)
    
    # Creating an instance of Solution
    solution = Solution()
    
    # Getting the right side view of the tree
    result = solution.rightSideView(root)
    
    # Printing the result
    print(result)  # Expected output: [1, 3, 6, 7]
