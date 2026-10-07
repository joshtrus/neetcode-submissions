from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()
        count = 0

        for i in range(n):
            graph[i] = []
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            

        for node in range(n):
            if node in visited:
                continue 
            
            count += 1
            visited.add(node)
            queue = deque([node])

            while queue:
                curr_node = queue.popleft()
                
                for nei in graph[curr_node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        
        return count
            

            

        
    
