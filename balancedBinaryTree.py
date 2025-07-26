from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findHeight(root):
            if root is None:
                return 0
            
            left = findHeight(root.left)
            if left == -1:
                return -1
            right = findHeight(root.right)
            if right == -1:
                return -1
                
            if abs(left-right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return findHeight(root) != -1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    sol = Solution()
    print(sol.isBalanced(root))