from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.mini = float('inf')

        def inOrder(root):
            if root is None:
                return
            
            inOrder(root.left)

            if self.prev is not None:
                self.mini = min(abs(self.prev.val-root.val), self.mini)
            
            self.prev = root

            inOrder(root.right)
        
        inOrder(root)
        return self.mini

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
    result = solution.minDiffInBST(root)
    print("Minimum distance:", result)