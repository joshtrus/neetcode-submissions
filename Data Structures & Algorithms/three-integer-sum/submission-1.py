class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sorted_nums = sorted(nums)
        
        

        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(sorted_nums) - 1


            while j < k:
                numsum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if numsum == 0:
                    res.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                
                elif numsum > 0:
                    k -= 1
                
                else:
                    j += 1
            
        
        return [list(x) for x in res]
                





    






        