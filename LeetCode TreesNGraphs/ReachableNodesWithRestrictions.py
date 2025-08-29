from collections import defaultdict


class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        seen = set()

        
        if not edges:
            return 1 if 0 not in restricted else 0

        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        restricted_set = set(restricted)
        seen = set()

        def dfs(node):
            if node in seen or node in restricted_set:
                return 0
            
            seen.add(node)
            count = 1

            for neighbour in graph[node]:
                count += dfs(neighbour)
            
            return count

        if 0 in restricted_set:
            return 0
        
        return dfs(0)
        
solution = Solution()

result = solution.reachableNodes(7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1])

print(result)