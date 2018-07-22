'''
参考：https://www.cnblogs.com/EdwardLiu/p/5100920.html

分析：假设当前node 为root

1. if value < root.val, 要被删除的节点在左子树，往左子树递归，并把操作结束后的返回值作为新的root.left

2. if value > root.val, 要被删除的节点在右子树，往右子树递归, 并把操作结束后的返回值作为新的root.right

3. if root == null, 递归到了一个null点，说明要删的value不存在，return null，而这个null点的parent的相应子树本来也是null，对树的结构没有任何影响

4. if value == root.val，说明root是该被删除的了

　　A. if root.left == null, return root.right

　　B. if root.right == null, return root.left(这两个case其实包含了只有一个child和一个child都没有的三种情况)

　　C. 如果两个children都存在，从右子树中找最小的node，与root交换，再递归调用函数在右子树中删除root.val

'''


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return None
        if root.val > value:
            root.left = self.removeNode(root.left, value)
        elif root.val < value:
            root.right = self.removeNode(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # find min in right child
            tn = root.right
            while tn.left:
                tn = tn.left
            tn.val, root.val = root.val, tn.val
            root.right = self.removeNode(root.right, value)
        return root
            
            