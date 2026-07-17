class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
     

            while j < k:
                triple_sum = nums[i] + nums[j] + nums[k] 

                if triple_sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif triple_sum > 0:
                    k -= 1
                else:
                    j +=1
        
        return [list(t) for t in res]




    






        