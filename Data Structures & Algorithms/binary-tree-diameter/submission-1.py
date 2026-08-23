# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            
            dl, hl = dfs(root.left)
            dr, hr = dfs(root.right)

            height = 1 + max(hl, hr)
            diameter = max(dl, dr, hl + hr)

            return (diameter, height)
        
        return dfs(root)[0]
            

