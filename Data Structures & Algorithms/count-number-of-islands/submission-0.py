from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(start, directions, visited):
            queue = deque(start)
            count = 1
            while queue:
                (curr_x, curr_y) = queue.popleft()
                visited.add((curr_x, curr_y))

                for direction in directions:
                    new_x, new_y = curr_x + direction[0], curr_y + direction[1]
                    if  ((new_x >= 0 and new_x < len(grid)) 
                    and (new_y >= 0 and new_y < len(grid[0]))
                    and (new_x, new_y) not in visited
                    and grid[new_x][new_y] == "1") :
                        queue.append((new_x, new_y))
                        count += 1
                        visited.add((new_x, new_y))
            
            return 1 if count > 0 else 0
        
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        visited = set()
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                    result += bfs([(r,c)] , directions, visited)
        
        return result
                    



        