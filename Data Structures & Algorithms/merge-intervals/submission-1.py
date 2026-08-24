class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()

        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        res = []
        
        for start, end in intervals[1:]:
            if start <= currEnd:
                currEnd = max(currEnd, end)
            else:
                res.append([currStart, currEnd])
                currStart = start
                currEnd = end
        
        res.append([currStart, currEnd])
        
        return res
        
