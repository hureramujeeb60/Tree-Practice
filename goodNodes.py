class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def isSolve(root, max_val):
            if root is None:
                return 
            
            if root.val >= max_val:
                self.count += 1
            
            new_maxi = max(root.val, max_val)

            isSolve(root.left, new_maxi)
            isSolve(root.right, new_maxi)
    
        isSolve(root, float('-inf'))
        return self.count