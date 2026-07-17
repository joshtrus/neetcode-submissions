class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_freq = {}

        for num in nums:
            map_freq[num] = map_freq.get(num, 0) + 1
        
        sorted_freq = sorted

        sorted_freq = sorted(map_freq, key=map_freq.get, reverse=True)

        return sorted_freq[:k]

        