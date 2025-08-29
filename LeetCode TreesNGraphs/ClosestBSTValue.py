import collections



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        closestValue = root.val
        bestDiff = abs(target - root.val)
        node = root

        while node is not None:

            if abs(target - node.val) < abs(target - closestValue):
                closestValue = node.val
            elif abs(target - node.val) == abs(target - closestValue):
                if node.val < closestValue:
                    closestValue = node.val

            
            if target == node.val:
                return node.val
            
            if target < node.val:
                node = node.left
            else:
                node = node.right
        
        return closestValue

        





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



input_nodes = [1]


root_node = build_tree(input_nodes)


solver = Solution()

result = solver.closestValue(root_node, 1)


print(result)