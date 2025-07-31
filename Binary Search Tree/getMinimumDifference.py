from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(self.prev-root.val))
            self.prev = root.val
            inOrder(root.right)
        
        inOrder(root)
        return self.min_diff
    
if __name__ == "__main__":
    # Construct a sample BST:
    #        4
    #       / \
    #      2   6
    #     / \
    #    1   3

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    solution = Solution()
    result = solution.getMinimumDifference(root)
    print("Minimum absolute difference:", result)
