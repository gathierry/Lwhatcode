'''
递归解法：返回左子树或者右子树中大的深度加1，作为自己的深度 （深度优先搜索）
非递归解法：采用层序遍历 （广度优先搜索）
'''

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1
        
    
        
from TreeNode import BinaryTree
if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([[1], [2, 3], ['N', 'N', 4, 5]])
    print(s.maxDepth(tree.root))