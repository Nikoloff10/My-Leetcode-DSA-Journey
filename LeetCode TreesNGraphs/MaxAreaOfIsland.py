# class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         graph= []
#         visited = []
#         max_area = 0

        
#         for i in range(len(grid)):
#             graph.append([str(cell) for cell in grid[i]])

#         rows = len(graph)
#         cols = len(graph[i])

#         for i in range(rows):
#             visited.append([False] * cols)

        

#         def dfs(row, col, graph, visited, island, max_area):
#             if row < 0 or col < 0 or row >= rows or col >= cols:
#                 return
#             if visited[row][col]:
#                 return
#             if graph[row][col] == "0":
#                 return

#             visited[row][col] = True

#             dfs(row-1, col, graph, visited, island, max_area)
#             dfs(row+1, col, graph, visited, island, max_area)
#             dfs(row, col-1, graph, visited, island, max_area)
#             dfs(row, col+1, graph, visited, island, max_area)

#             if graph[row][col] == "1":
#                 island.append(graph[row][col])
                
#         for row in range(rows):
#             for col in range(cols):
#                 if visited[row][col]:
#                     continue
#                 island = []
#                 dfs(row, col, graph, visited, island, max_area)
                
#                 if len(island) > 0 and max_area < len(island):
#                     max_area = len(island)
                    
#         return max_area



        
        

        

# solution = Solution()

# result = solution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]])

# print(result)
# OPTIMIZED CODE BELOW

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        max_area = 0

        def dfs(row, col):
         
            if (row < 0 or col < 0 or row >= rows or col >= cols or 
                visited[row][col] or grid[row][col] == 0):
                return 0
            
           
            visited[row][col] = True
            
            
            area = 1
            area += dfs(row - 1, col)  
            area += dfs(row + 1, col)  
            area += dfs(row, col - 1)  
            area += dfs(row, col + 1)  
            
            return area
        
        
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == 1:
                    current_area = dfs(row, col)
                    max_area = max(max_area, current_area)
        
        return max_area


solution = Solution()

result = solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(result)


result2 = solution.maxAreaOfIsland([[1,1,0,0,0],
                                   [1,1,0,0,0],
                                   [0,0,0,1,1],
                                   [0,0,0,1,1]])
print(result2)