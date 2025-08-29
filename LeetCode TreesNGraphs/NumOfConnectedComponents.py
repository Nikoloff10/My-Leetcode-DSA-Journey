from collections import defaultdict


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0
        def dfs(node):
            if visited[node] == True:
                return
            visited[node] = True

            for neighbour in graph[node]:
                dfs(neighbour)
        

        for i in range(n):
            if visited[i] == False:
                count+=1
                visited[i] == True
                dfs(i)
            

        return count

        


solution = Solution()
result = solution.countComponents(5, [[0,1],[1,2],[3,4]])
print(result)