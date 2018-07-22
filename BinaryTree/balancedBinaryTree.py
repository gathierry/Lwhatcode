'''
递归检测每个子树的深度，如果差小于等于 1，返回深度
如果差大于 1，返回 -1
'''


class Solution:
    def checkDepth(self, root):
        if root is None:
            return 0
        l = self.checkDepth(root.left)
        if l == -1:
            return -1 
        r = self.checkDepth(root.right)
        if r == -1:
            return -1 
        diff = abs(l - r)
        return -1 if diff > 1 else 1 + max(l, r)
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.checkDepth(root) != -1
        