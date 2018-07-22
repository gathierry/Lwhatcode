


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node
        tn = root
        while tn:
            if tn.val > node.val:
                if tn.left:
                    tn = tn.left
                else:
                    tn.left = node
                    return root
            else:
                if tn.right:
                    tn = tn.right
                else:
                    tn.right = node
                    return root
                    
from TreeNode import TreeNode, BinaryTree
if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([[2], [1, 4], [None, None, 3, None]])
    node = TreeNode(6)
    root = s.insertNode(tree.root, node)
    root.printTreeFrom()
    