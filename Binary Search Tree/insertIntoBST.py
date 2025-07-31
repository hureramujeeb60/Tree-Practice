from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Helper method to print the tree in-order (for verification)
    def in_order(self):
        result = []
        if self.left:
            result.extend(self.left.in_order())
        result.append(self.val)
        if self.right:
            result.extend(self.right.in_order())
        return result


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)

    solution = Solution()
    updated_root = solution.insertIntoBST(root, 5)

    print("In-order traversal after insertion:", updated_root.in_order())
        
