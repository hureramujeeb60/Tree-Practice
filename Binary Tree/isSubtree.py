from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isValid(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
    

    def isValid(self, p,q):
        if p is None and q is None:
            return True
        
        if p is None or q is None or p.val != q.val:
            return False
        
        return self.isValid(p.left, q.left) and self.isValid(p.right, q.right)
