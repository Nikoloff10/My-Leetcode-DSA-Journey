from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        n_squared = n * n
        
        
        def square_to_pos(square):
            
            square -= 1
            row = n - 1 - (square // n)
            if (n - 1 - row) % 2 == 0:  
                col = square % n
            else:  
                col = n - 1 - (square % n)
            return row, col
        
        
        queue = deque([(1, 0)])  
        visited = set([1])
        
        while queue:
            curr, rolls = queue.popleft()
            
            
            if curr == n_squared:
                return rolls
            
            
            for roll in range(1, 7):
                next_square = curr + roll
                if next_square > n_squared:
                    continue
                
                
                row, col = square_to_pos(next_square)
                
                
                if board[row][col] != -1:
                    final_square = board[row][col]
                else:
                    final_square = next_square
                
                
                if final_square not in visited:
                    visited.add(final_square)
                    queue.append((final_square, rolls + 1))
        
        
        return -1


solution = Solution()


board1 = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(solution.snakesAndLadders(board1))  


board2 = [[-1,-1],[-1,3]]
print(solution.snakesAndLadders(board2))  

