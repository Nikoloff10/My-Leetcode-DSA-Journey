import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root






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



input_nodes = [4,2,7,1,3]


root_node = build_tree(input_nodes)


solver = Solution()

result = solver.insertIntoBST(root_node, 5)


print(result)