from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderTraversalRecursive(root, result)
        return result

    def inorderTraversalRecursive(self, node: TreeNode, result: List[int]):
        if node:
            # Traverse left subtree
            self.inorderTraversalRecursive(node.left, result)
            # Visit the root node
            result.append(node.val)
            # Traverse right subtree
            self.inorderTraversalRecursive(node.right, result)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
solution.inorderTraversal(root)
