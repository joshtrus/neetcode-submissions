class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        for x in range(n):
            parent[x] = x

        def find(parent, x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            parent[root_y] = root_x
        
        for edge in edges:
            union(parent, edge[0], edge[1])
        
        roots = set()
        for node in parent:
            roots.add(find(parent, node))
        
        return len(roots)

        