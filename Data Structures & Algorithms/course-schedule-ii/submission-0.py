from collections import deque 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        degrees = {}
        res = []
        taken = deque()
        processed = 0

        for course in range(numCourses):
            graph[course] = []
            degrees[course] = 0
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            degrees[child] += 1
        
        for child in degrees:
            if degrees[child] == 0:
                taken.append(child)
                res.append(child)

        while taken:
            node = taken.popleft()
            processed += 1

            for child in graph[node]:
                degrees[child] -= 1

                if degrees[child] == 0:
                    taken.append(child)
                    res.append(child)
        
        return res if processed == numCourses else []


                
        


        