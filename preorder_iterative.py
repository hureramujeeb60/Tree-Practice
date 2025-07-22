from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root)

        while stack:
            cur_el = stack.pop()
            res.append(cur_el.val)

            if cur_el.right is not None:
                stack.append(cur_el.right)
            if cur_el.left is not None:
                stack.append(cur_el.left)
            
        return res

if __name__ == "__main__":
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.right.left = TreeNode(3)
    sol = Solution()
    res = sol.preorderTraversal(node)
    print(res)