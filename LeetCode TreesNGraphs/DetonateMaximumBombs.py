from collections import defaultdict
from math import sqrt


class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)
        
        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for nei in graph[i]:
                dfs(nei, visit)
            return len(visit)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res
    
solution = Solution()
result = solution.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])
print(result)