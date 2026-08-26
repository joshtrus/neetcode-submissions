# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Assumptions
        #-------------------------------------
        #longest path either left or right
        #tree with only root returns depth 1


        #Clarifying Questions
        #-------------------------------------
        # Does amount of children affect depth

        #Approach
        #-------------------------------------
        #recursive approach
        #call function on left and right + 1
        #return max of whichever
        #Time complexity O(n) Space complexity of O(1) because nothing is stored. happening in line

        #Better Approach
        #-------------------------------------

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        
