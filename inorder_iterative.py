from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        stack = []

        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            res.append(cur.val)

            cur = cur.right
        
        return res

if __name__ == "__main__":
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.left = TreeNode(4)
    node.right.left = TreeNode(3)
    sol = Solution()
    res = sol.inorderTraversal(node)
    print(res)