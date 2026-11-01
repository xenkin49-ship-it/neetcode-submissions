# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def switch(root):
            if not root:
                return
            switch(root.left)
            switch(root.right)
            root.left,root.right=root.right,root.left
        switch(root)
        return root