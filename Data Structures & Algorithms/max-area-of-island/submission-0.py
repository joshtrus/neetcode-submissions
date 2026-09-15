from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Clarifying Questions


        #Assumptions


        #Possible Solution
        


        #Better Solution

        def bfs(start, directions, visited):
            queue = deque([start])
            visited.add(start)
            count = 1

            while queue:
                (curr_x, curr_y) = queue.popleft()

                for direction in directions:
                    new_x, new_y = curr_x + direction[0], curr_y + direction[1]

                    if (
                        new_x >= 0 and new_x < len(grid)
                        and new_y >= 0 and new_y < len(grid[0])
                        and (new_x, new_y) not in visited
                        and grid[new_x][new_y] == 1
                    ):
                        count +=1
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
            
            return count 
        
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        max_size = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (
                    (r,c) not in visited
                    and grid[r][c] == 1
                ):
                    size = bfs((r,c), directions, visited)
                    max_size = max(size, max_size)
        
        return max_size




        