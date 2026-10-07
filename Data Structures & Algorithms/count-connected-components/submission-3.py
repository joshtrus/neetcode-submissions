from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()
        count = 0

        for i in range(n):
            graph[i] = []
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

         

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
            

            

        
    
