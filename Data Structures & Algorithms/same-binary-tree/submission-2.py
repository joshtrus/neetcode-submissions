# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case

        if not p and not q:
            return True

        if not p or not q :
                return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  
        






        #recursive step
        

     
    #current node is equal in both trees
    #if tree is just a root then its equal
    #if a node is null/doesnt exist, it should be equal on the other side
    #null node is not equal an actual node, will return false
    #the placement of the nodes matter
        