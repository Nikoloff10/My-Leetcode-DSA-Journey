import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if root == None:
            return 0
        
        self.diff = 0

        def dfs(node, curr_min, curr_max):

            if not node:
                return
            
            self.diff = max(self.diff, abs(node.val - curr_min), abs(node.val - curr_max))

            new_min_children = min(curr_min, node.val)
            new_max_children = max(curr_max, node.val)

            dfs(node.left, new_min_children, new_max_children)
            dfs(node.right, new_min_children, new_max_children)

        dfs(root, root.val, root.val)

        return self.diff

def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        current_node = queue.popleft()

        
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1


        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root


solver = Solution()


input_nodes = [8,3,10,1,6,None,14,None,None,4,7,13]


root_node = build_tree(input_nodes)


result = solver.maxAncestorDiff(root_node)


print(result)