'''
采用递归，先打印当前 node，再打印左子树，再打印右子树
Challenge Can you do it without recursion?
使用栈，输入根节点，如果左节点存在就一直进栈，遇到 None 时，转到栈顶元素的右节点

https://blog.csdn.net/zhangxiangDavaid/article/details/37115355
'''


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        st = []
        res = []
        tn = root
        while tn or len(st) > 0:
            if tn:
                st.append(tn)
                res.append(tn.val)
                tn = tn.left
            else:
                top = st.pop()
                tn = top.right
        return res
        
    def inorderTraversal(self, root):
        # write your code here
        st = []
        res = []
        tn = root
        while tn or len(st) > 0:
            if tn:
                st.append(tn)
                tn = tn.left
            else:
                top = st.pop()
                res.append(top.val)
                tn = top.right
        return res
        
    def postorderTraversal(self, root):
        # write your code here
        st = []
        res = []
        tn = root
        lastVisit = None
        # go to the bottom of left tree
        while tn:
            st.append(tn)
            tn = tn.left
        while len(st) > 0:
            top = st.pop()
            # if no right child or right child is visitied, then visit current node
            if top.right is None or top.right is lastVisit:
                res.append(top.val)
                lastVisit = top
            else:
                st.append(top)
                tn = top.right
                while tn:
                    st.append(tn)
                    tn = tn.left
        return res
                
            
            
        
        
        
from TreeNode import BinaryTree
if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([[1], [2, 3], [4, 5, None, None]])
    tree = BinaryTree([[1], [2, 3], [4, None, None, 5], [None, 6, None, None, None, None, None, None], [None, None, 7, 8, None, None, None, None, None, None, None, None, None, None, None, None]])
    print(s.preorderTraversal(tree.root))
        
        
        