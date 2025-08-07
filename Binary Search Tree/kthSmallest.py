from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def inOrder(root):
            if root is None:
                return None
            
            left = inOrder(root.left)
            if left is not None:
                return left
            self.count += 1

            if self.count == k:
                return root.val

            return inOrder(root.right)
        
        return inOrder(root)

if __name__ == "__main__":
    # Construct the binary search tree (BST)
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    k = 3  # We are looking for the 3rd smallest element

    solution = Solution()
    result = solution.kthSmallest(root, k)

    print(f"The {k}rd smallest element in the BST is: {result}")
