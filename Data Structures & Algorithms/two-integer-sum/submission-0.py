class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for i, num in enumerate(nums):
            diff = target - num

            if num in seen:
                return [nums.index(diff), i]
            seen.add(diff)

        