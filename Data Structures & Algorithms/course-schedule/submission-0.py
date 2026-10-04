from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        degrees = {}
        taken = deque()
        count = 0

        for course in range(numCourses):   
            graph[course] = []               
            degrees[course] = 0            


        for child, parent in prerequisites:
            graph[parent].append(child)
            degrees[child] += 1

        for child in degrees:
            if degrees[child] == 0:
                taken.append(child)
        
        while taken:
            node = taken.popleft()
            count += 1

            for child in graph[node]:
                degrees[child] -= 1

                if degrees[child] == 0:
                    taken.append(child)
        
        return count == numCourses
            
            

        
        







            


        


        