# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs (node, cumsum):
            if not node:
                return False
            cumsum += node.val
            if cumsum == targetSum and not node.left and not node.right:
                return True
            return dfs(node.left, cumsum) or dfs(node.right, cumsum)
        return dfs(root, 0)