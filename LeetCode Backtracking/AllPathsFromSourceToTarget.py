class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, path):
            path.append(node)
            if node == len(graph) - 1:
                result.append(path[:])
            else:
                for neighbor in graph[node]:
                    dfs(neighbor, path)
            path.pop()
        
        result = []
        dfs(0, [])
        return result        


        

solution = Solution()
result = solution.allPathsSourceTarget([[1,2],[3],[3],[]])
print(result)