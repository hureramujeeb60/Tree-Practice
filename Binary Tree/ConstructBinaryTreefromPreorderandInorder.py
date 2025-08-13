from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        inOrderIdx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+inOrderIdx], inorder[:inOrderIdx])
        root.right = self.buildTree(preorder[1+inOrderIdx:], inorder[inOrderIdx+1:])

        return root


def print_inorder(root: Optional[TreeNode]):
    if root:
        print_inorder(root.left)
        print(root.val, end=' ')
        print_inorder(root.right)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    sol = Solution()
    tree_root = sol.buildTree(preorder, inorder)

    print("Inorder traversal of the constructed tree:")
    print_inorder(tree_root)
    print() 
