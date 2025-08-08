from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        
        else:
            if not root.right:
                return root.left
            
            elif not root.left:
                return root.right
            
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        
        return root
    
def inorder_traversal(root: Optional[TreeNode]):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

if __name__ == "__main__":
    # Build the following BST:
    #        5
    #       / \
    #      3   6
    #     / \   \
    #    2   4   7
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    print("Original tree (in-order):")
    inorder_traversal(root)
    print()

    key_to_delete = 3
    print(f"\nDeleting node with key = {key_to_delete}")

    sol = Solution()
    root = sol.deleteNode(root, key_to_delete)

    print("\nTree after deletion (in-order):")
    inorder_traversal(root)
    print()
    