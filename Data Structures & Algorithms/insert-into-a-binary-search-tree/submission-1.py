# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        def recursive_insertion(cur,val):
            if cur.val<val:
                if not cur.right:
                    cur.right=TreeNode(val)
                else:
                    recursive_insertion(cur.right,val)
            else:
                if not cur.left:
                    cur.left=TreeNode(val)
                else:
                    recursive_insertion(cur.left,val)
        recursive_insertion(root,val)
        return root