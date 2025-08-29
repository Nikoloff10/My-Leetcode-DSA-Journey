
from collections import deque
import collections
import queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sum = 0
        deepest_nodes = []
        if root is None:
            return

        queue = deque([root])
        
        while queue:
            current_length = len(queue)
            curr_level = []
            
            for _ in range(current_length):
                node = queue.popleft()
                curr_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            deepest_nodes = curr_level
        for node in deepest_nodes:
            sum += node.val
        return sum
    
def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    q = collections.deque([root])
    i = 1

    while q and i < len(nodes):
        current_node = q.popleft()

   
        if i < len(nodes) and nodes[i] is not None: 
            current_node.left = TreeNode(nodes[i])
            q.append(current_node.left)
        i += 1 

       
        if i < len(nodes) and nodes[i] is not None: 
            current_node.right = TreeNode(nodes[i])
            q.append(current_node.right)
        i += 1 

    return root



input_nodes = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]


root_node = build_tree(input_nodes)


solver = Solution()

result = solver.deepestLeavesSum(root_node)


print(result)