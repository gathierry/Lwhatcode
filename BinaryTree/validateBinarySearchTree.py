'''
要注意，子节点不仅要和父节点比，还可能要和再上一级的节点比
e.g.
        5
    2        6
1      x

x 一定大于 2 且 x 必须小于 5
'''

class Solution:
    def isValidSubtree(self, root, min=None, max=None):
        if root is None:
            return True
        tn = root
        l, r = True, True
        if tn.left:
            if tn.left.val >= tn.val:
                return False
            if min:
                if tn.left.val <= min:
                    return False
            l = self.isValidSubtree(tn.left, max=tn.val)
        if tn.right:
            if tn.right.val <= tn.val:
                return False
            if max:
                if tn.right.val >= max:
                    return False
            r = self.isValidSubtree(tn.right, min=tn.val)
        return l and r
        
    
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        return self.isValidSubtree(root)
        
        
from TreeNode import BinaryTree
if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([[2], [1, 4], [None, None, 3, 5]])
    tree = BinaryTree([[10],[5, 15],[None, None, 6, 20]])
    print(s.isValidBST(tree.root))
            