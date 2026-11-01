# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if root.val==subRoot.val:
            if self.issame(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def issame(self,p,r):
        if not p and not r:
            return True
        if not p or not r or p.val!=r.val:
            return False
        return self.issame(p.left,r.left) and self.issame(p.right,r.right)