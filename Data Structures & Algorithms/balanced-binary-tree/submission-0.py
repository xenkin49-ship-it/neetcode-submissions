# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            if height(node.left)==-1:
                return -1
            elif height(node.right)==-1:
                return -1
            if abs(height(node.left)-height(node.right))>1:
                return -1
            return max(height(node.left),height(node.right))+1
        return True if height(root)!=-1 else False