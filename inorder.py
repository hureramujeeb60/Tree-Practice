from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def traverse(root):
            if root is None:
                return

            traverse(root.left)
            lst.append(root.val)
            traverse(root.right)
            
        traverse(root)
        return lst
    
    
if __name__ == "__main__":
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.right.left = TreeNode(3)
    sol = Solution()
    res = sol.postorderTraversal(node)
    print(res)