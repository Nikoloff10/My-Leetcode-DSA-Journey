import collections


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        if source == destination:
            return True

        
        
        adj = collections.defaultdict(list)
        for u, v in edges:
            
            adj[u].append(v)
            adj[v].append(u)

        
        queue = collections.deque([source])
        visited = {source}

        
        while queue:
            
            current_node = queue.popleft()

            
            for neighbor in adj[current_node]:
                
                if neighbor == destination:
                    return True
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        
        return False



if __name__ == "__main__":
    solver = Solution()

    
    
    n1 = 3
    edges1 = [[0, 1], [1, 2]]
    source1, destination1 = 0, 2
    result1 = solver.validPath(n1, edges1, source1, destination1)
    print(f"Test Case 1: Path from {source1} to {destination1}? -> {result1}") 

    
    
    n2 = 6
    edges2 = [[0, 1], [1, 2], [3, 4], [4, 5]]
    source2, destination2 = 0, 5
    result2 = solver.validPath(n2, edges2, source2, destination2)
    print(f"Test Case 2: Path from {source2} to {destination2}? -> {result2}") 

    
    n3 = 3
    edges3 = [[0, 1], [1, 2]]
    source3, destination3 = 1, 1
    result3 = solver.validPath(n3, edges3, source3, destination3)
    print(f"Test Case 3: Path from {source3} to {destination3}? -> {result3}") 

    
    
    n4 = 3
    edges4 = [[0, 1], [1, 2], [2, 0]]
    source4, destination4 = 0, 2
    result4 = solver.validPath(n4, edges4, source4, destination4)
    print(f"Test Case 4: Path from {source4} to {destination4}? -> {result4}") 
