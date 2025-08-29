import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        queue = collections.deque([root])
        
        
        isLeft = True
        result = []

        while queue:
            curr_level = []
            current_length = len(queue)

            for _ in range(current_length):

                node = queue.popleft()
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not isLeft:
                curr_level.reverse()
            result.append(curr_level)

            isLeft = not isLeft
        return result
            
                
 




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



input_nodes = [3,9,20,None,None,15,7]


root_node = build_tree(input_nodes)


solver = Solution()

result = solver.zigzagLevelOrder(root_node)


print(result)