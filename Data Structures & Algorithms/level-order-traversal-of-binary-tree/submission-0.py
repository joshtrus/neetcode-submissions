from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Assumptions
        #-------------------------------
        #each sublist represents a level
        #empty -> []



        #Clarifying Questions
        #-------------------------------
        #If a node child is null do we represent it as null in level or no




        #Possible Approach
        #-------------------------------
        #bfs w/ queue
        #size of queue at given time is amount of nodes in a list
        #Time complexity of O(n) where n is number of nodes
        #Space complexity of O(n)


        #Better Approach
        #-------------------------------
        if not root:
            return[]
         
        result = []
        queue = deque([root])

        while queue:
            level = []
            levelSize = len(queue)

            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
                    








        