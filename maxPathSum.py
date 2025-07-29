from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def solve(root):
            if root is None:
                return 0
            
            left = max(0, solve(root.left))
            right = max(0, solve(root.right))

            self.maxi = max(root.val + left + right, self.maxi)

            return root.val + max(left, right)
        
        solve(root)
        return self.maxi

if __name__ == "__main__":
    from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def solve(root):
            if root is None:
                return 0
            
            left = max(0, solve(root.left))
            right = max(0, solve(root.right))

            self.maxi = max(root.val + left + right, self.maxi)

            return root.val + max(left, right)
        
        solve(root)
        return self.maxi

if __name__ == "__main__":
    # Example Tree:
    #       -10
    #       /  \
    #      9   20
    #         /  \
    #        15   7

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    result = sol.maxPathSum(root)
    print("Maximum Path Sum:", result)
