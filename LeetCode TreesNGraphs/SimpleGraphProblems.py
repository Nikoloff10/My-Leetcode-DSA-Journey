from collections import defaultdict
from typing import List


def find_most_connected(edges: List[List[int]]) -> int:
    """
    Finds the node with the highest degree (most connections) in a graph.

    Args:
        edges: A list of edges representing the connections in the graph.

    Returns:
        The node with the highest degree. If there's a tie, any of the
        nodes with the highest degree can be returned.
    """
    # Hint 1: You will need to build an adjacency list first, just like
    # in the FindIfPathExistsInGraph problem.

    # Hint 2: After building the adjacency list, you can iterate through it.
    # For each node in the adjacency list, the number of its neighbors
    # is len(adj[node]).

    # Hint 3: Keep track of the node with the most neighbors seen so far.

    # --- YOUR CODE GOES HERE ---

    if not edges:
        return -1

    adjacent_list = defaultdict(list)
    

    for i, j in edges:
        adjacent_list[i].append(j)
        adjacent_list[j].append(i)
    
    most_connected_node = -1
    max_degree = -1

    for node, neighbours in adjacent_list.items():
        if len(neighbours) > max_degree:
            max_degree = len(neighbours)
            most_connected_node = node
    return most_connected_node
    


# --- Test Cases ---
if __name__ == "__main__":
    # Test Case 1:
    # Graph: 0 -- 1 -- 2
    #         |  /
    #         3
    # Degrees: 0:2, 1:3, 2:1, 3:2. Node 1 has the highest degree.
    edges1 = [[0, 1], [1, 2], [1, 3], [0, 3]]
    print(f"Test Case 1: Most connected node is {find_most_connected(edges1)}")  # Expected: 1

    # Test Case 2:
    # Graph: 0 -- 1, 2 -- 3
    edges2 = [[0, 1], [2, 3]]
    print(f"Test Case 2: Most connected node is {find_most_connected(edges2)}")  # Expected: 0, 1, 2, or 3 (all have degree 1)