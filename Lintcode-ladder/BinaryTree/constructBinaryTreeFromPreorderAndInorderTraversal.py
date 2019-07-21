'''
参考：https://siddontang.gitbooks.io/leetcode-solution/content/tree/construct_binary_tree.html
                1
        --------|-------
        2               3
    ----|----       ----|----
    4       5       6       7

前序遍历 1245367
中序遍历 4251637
后续遍历 4526731

需要掌握的性质：
前序：第一个元素是根节点
中序：根节点前为左子树，后为右子树
后序：最后一个元素是根节点

若已知的是 中序 后序
后序遍历的最后一个元素 1 是根节点 -> 中序里找到 1，左边是左子树，右边是右子树。
中序 425 1 637
后序 452   673 1
在后序相对应的位是子树，再分别取根节点 2，3，以此类推

若已知的是 前序 中序
前序遍历的第一个元素 1 是根节点 -> 中序里找到 1，左边是左子树，右边是右子树。
前序 1 245   367
中序   425 1 637
在前序相对应的位是子树，再分别取根节点 2，3，以此类推
'''

from TreeNode import TreeNode

class Solution:    
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree2(self, preorder, inorder):
        # write your code here
        if len(preorder) == 0:
            return None
        root = preorder[0]
        indx = inorder.index(root)
        left, right = None, None
        if indx > 0:
            left = self.buildTree2(preorder[1:indx+1], inorder[:indx])
        if indx < len(inorder) - 1:
            right = self.buildTree2(preorder[indx+1:], inorder[indx+1:])
        rootNode = TreeNode(root)
        rootNode.left = left
        rootNode.right = right
        return rootNode
        
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        root = postorder[-1]
        indx = inorder.index(root)
        left, right = None, None
        if indx > 0:
            left = self.buildTree(inorder[:indx], postorder[:indx])
        if indx < len(inorder) - 1:
            right = self.buildTree(inorder[indx+1:], postorder[indx:-1])
        rootNode = TreeNode(root)
        rootNode.left = left
        rootNode.right = right
        return rootNode
        
        
from TreeNode import BinaryTree
if __name__ == '__main__':
    s = Solution()
    root = s.buildTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
    root.printTreeFrom()
        
        
        