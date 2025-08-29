from collections import defaultdict, deque
from typing import List

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """        
        
        def dfs(node):
            for neighbour in graph[node]:

                if neighbour not in seen:
                    seen.add(neighbour)
                    print(neighbour)
                    dfs(neighbour)
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            for j in range(i + 1, n):
                if edges[i]:
                    graph[i].append(j)
                    graph[j].append(i)

        
        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:

                ans += 1
                seen.add(i)
                dfs(i)
        return ans


        

if __name__ == "__main__":
    solver = Solution()
    
   
    n_test1 = 5
    edges_test1 = [[0,1],[1,2],[3,4]]
    result1 = solver.countComponents(n_test1, edges_test1)
    print(f"Test Case 1: For n={n_test1}, edges={edges_test1}")
    print(f"Got: {result1}")
   
    
    