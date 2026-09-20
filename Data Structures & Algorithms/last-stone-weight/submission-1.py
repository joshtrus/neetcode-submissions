import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Clarifying Questions



        #Assumptions


        #Possible Solution
        heap = []

        for stone in stones:
            heapq.heappush(heap, stone * -1)
        
        while len(heap) > 1:
            x = heapq.heappop(heap) 
            y = heapq.heappop(heap)

            if x != y:
                new_y = x - y
                heapq.heappush(heap, new_y)
        
        return -heap[0] if heap else 0



        #Better Solution

        