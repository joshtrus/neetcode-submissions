# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Assumption
        #-----------------------------
        #value is unqiue
        #Ancestor can be descendent of itself
        #Target node has children p and q or is either p or q


        #Clarifying Question
        #-----------------------------




        #Possible Approach
        #------------------------------
        #dfs returns if p or q is found 
        



        #Better Approach
        #------------------------------
        
        def dfs(root):
            if not root or root == p or root == q:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            else:
                return left or right
        
        return dfs(root)