from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        maxiWidth = 0

        while q:
            level_size = len(q)
            stIdx = q[0][1]
            endIdx = q[-1][1]
            maxiWidth = max(maxiWidth, (endIdx - stIdx) + 1)

            for _ in range(level_size):
                node, idx = q.popleft()
                if node.left is not None:
                    q.append((node.left, 2*idx+1))
                if node.right is not None:
                    q.append((node.right, 2*idx+2))

        return maxiWidth
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(9)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    sol = Solution()
    print(sol.widthOfBinaryTree(root))