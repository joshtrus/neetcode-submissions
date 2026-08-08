class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            bucket[count].append(num)

        for i in range(len(bucket) -1, 0, -1):
            res.extend(bucket[i])

            if len(res) >= k:
                return res



     




