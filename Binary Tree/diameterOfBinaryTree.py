from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def findHeight(root):
            if root is None:
                return 0

            left = findHeight(root.left)
            right = findHeight(root.right)

            self.max_diameter = max(self.max_diameter, left+right)
                    
            return max(left, right) + 1

        findHeight(root)
        return self.max_diameter

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))