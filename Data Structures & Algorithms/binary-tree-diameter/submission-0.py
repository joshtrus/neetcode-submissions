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
                return (0,0)
            
            (ld, lh) = dfs(root.left)
            (rd, rh) = dfs(root.right)

            height = 1 + max(lh, rh)
            diameter = max(ld, rd, lh + rh)

            return (diameter, height)


        return dfs(root)[0]


    

        