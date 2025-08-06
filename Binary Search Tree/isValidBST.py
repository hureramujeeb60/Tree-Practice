from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None

        def inOrder(root):
            if root is None:
                return True
            
            if not inOrder(root.left):
                return False
            
            if self.prev is not None and self.prev >= root.val:
                return False
            
            self.prev = root.val
            
            return inOrder(root.right)
        
        return inOrder(root)

if __name__ == "__main__":
    # Example of a valid BST:
    #       2
    #      / \
    #     1   3

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print("Is the tree a valid BST?", sol.isValidBST(root))