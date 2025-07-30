from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

if __name__ == "__main__":
    # Construct the binary search tree
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    val_to_search = 2

    sol = Solution()
    result = sol.searchBST(root, val_to_search)

    if result:
        print(f"Found node with value: {result.val}")
    else:
        print("Value not found in the tree.")
