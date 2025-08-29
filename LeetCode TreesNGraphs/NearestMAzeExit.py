# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         if grid[0][0] == 1:
#             return -1
        
#         def valid(row, col):
#             return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
#         n = len(grid)
#         seen = {(0, 0)}
#         queue = deque([(0, 0, 1)]) # row, col, steps
#         directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
        
#         while queue:
#             row, col, steps = queue.popleft()
#             if (row, col) == (n - 1, n - 1):
#                 return steps
            
#             for dx, dy in directions:
#                 next_row, next_col = row + dy, col + dx
#                 if valid(next_row, next_col) and (next_row, next_col) not in seen:
#                     seen.add((next_row, next_col))
#                     queue.append((next_row, next_col, steps + 1))
        
#         return -1

from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        starting_row, starting_col = entrance[0], entrance[1]
        rows = len(maze)
        cols = len(maze[0])

        if maze[starting_row][starting_col] == '+':
            return -1

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and maze[row][col] == '.' 
        
        
        seen = {(starting_row, starting_col)}
        queue = deque([(starting_row, starting_col, 0)])
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]


        while queue:
            row, col, steps = queue.popleft()
    
            if (row == rows - 1 or row == 0 or col == cols - 1 or col == 0) and (row, col) != (starting_row, starting_col):
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        return -1

        

solution = Solution()
result = solution.nearestExit([[".","+"]], [0,0])
print(result)