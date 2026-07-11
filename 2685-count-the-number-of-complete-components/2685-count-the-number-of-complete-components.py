from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        components = []
        
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                visited[i] = True
                comp = []
                while q:
                    v = q.popleft()
                    comp.append(v)
                    for nei in adj[v]:
                        if not visited[nei]:
                            visited[nei] = True
                            q.append(nei)
                components.append(comp)
        
        complete_count = 0
        for comp in components:
            k = len(comp)
            comp_set = set(comp)
            edge_count = 0
            for u, v in edges:
                if u in comp_set and v in comp_set:
                    edge_count += 1
            if edge_count == k * (k - 1) // 2:
                complete_count += 1
        
        return complete_count