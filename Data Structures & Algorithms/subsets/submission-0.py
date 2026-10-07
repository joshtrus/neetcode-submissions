class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def dfs(node, path):
            if node == len(nums):
                res.append(path.copy())
                return 
            
            path.append(nums[node])
            dfs(node + 1, path)
            path.pop()

            dfs(node + 1, path)

        dfs(0, [])
        return res


            
        