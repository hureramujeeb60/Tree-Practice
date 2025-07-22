from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            q_level = len(q)
            level = []

            for _ in range(q_level):
                node = q.popleft()
                level.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            res.append(level)

        return res    

if __name__ == "__main__":
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.left = TreeNode(4)
    node.right.left = TreeNode(3)
    sol = Solution()
    res = sol.levelOrder(node)
    print(res)

