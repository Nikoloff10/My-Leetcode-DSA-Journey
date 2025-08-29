from collections import defaultdict, deque
from typing import List, Set


def find_nodes_within_k_distance(edges: List[List[int]], start_node: int, k: int) -> Set[int]:
    """
    Finds all nodes that are at most k distance (hops) away from a start_node.

    Args:
        edges: A list of edges representing the connections in the graph.
        start_node: The node from which to start the search.
        k: The maximum distance (number of hops) to search.

    Returns:
        A set of all nodes within k distance of the start_node. The start_node
        itself should not be in the result set.
    """
    # Hint 1: Start by building an adjacency list for the graph.

    # Hint 2: Use a Breadth-First Search (BFS) approach. A queue is perfect for this.

    # Hint 3: You need to keep track of two things for each item in the queue:
    # the node itself AND its distance from the start_node. A good way to do
    # this is to store tuples in the queue, like: queue.append((node, distance)).

    # Hint 4: You'll also need a `visited` set to avoid visiting the same
    # node multiple times or getting stuck in cycles. Add the start_node to it
    # before the loop begins.

    # --- YOUR CODE GOES HERE ---

    if k == 0:
        return set()

    adj = defaultdict(list)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    if start_node not in adj:
        return set()

    
    queue = deque([(start_node, 0)])
    visited = {start_node}
    result = set()

    while queue:
        curr_node, curr_distance = queue.popleft()

        for neighbor in adj[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result.add(neighbor)

                if curr_distance + 1 < k:
                    queue.append((neighbor, curr_distance + 1))
    return result

    





# --- Test Cases ---
if __name__ == "__main__":
    # Test Case 1:
    # Graph: 0 -- 1 -- 2 -- 3 -- 4
    # Start: 0, k: 2
    # Nodes at dist 1: {1}
    # Nodes at dist 2: {2}
    # Expected result: {1, 2}
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    result1 = find_nodes_within_k_distance(edges1, start_node=0, k=2)
    print(f"Test Case 1: Nodes within 2 hops of 0 are {result1}")  # Expected: {1, 2}

    # Test Case 2:
    # Graph: A more complex graph
    #         0 -- 1 -- 2
    #         |  /
    #         3 -- 4
    # Start: 0, k: 1
    # Expected result: {1, 3}
    edges2 = [[0, 1], [1, 2], [0, 3], [1, 3], [3, 4]]
    result2 = find_nodes_within_k_distance(edges2, start_node=0, k=1)
    print(f"Test Case 2: Nodes within 1 hop of 0 are {result2}")  # Expected: {1, 3}

    # Test Case 3: k=0, should return an empty set
    result3 = find_nodes_within_k_distance(edges2, start_node=0, k=0)
    print(f"Test Case 3: Nodes within 0 hops of 0 are {result3}")  # Expected: set()

    # Test Case 4: Start node not in graph (should not crash)
    result4 = find_nodes_within_k_distance(edges2, start_node=99, k=2)
    print(f"Test Case 4: Nodes within 2 hops of 99 are {result4}") # Expected: set()