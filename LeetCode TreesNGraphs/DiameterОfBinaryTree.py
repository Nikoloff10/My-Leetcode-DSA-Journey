import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.diameter = 0
        def treeHeight(root):
            if root is None:
                return 0
            else:
                leftHeight = treeHeight(root.left)
                rightHeight = treeHeight(root.right)

                curr_diameter = leftHeight + rightHeight
                self.diameter = max(self.diameter, curr_diameter)

                return 1 + max(leftHeight, rightHeight)
        treeHeight(root)
        return self.diameter




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


input_nodes = [1,2]


root_node = build_tree(input_nodes)


result = solver.diameterOfBinaryTree(root_node)


print(result)