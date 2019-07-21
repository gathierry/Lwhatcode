'''
这道题用中序遍历可以递增地读出所有节点
'''

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
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
                if top.val >= k1 and top.val <= k2:
                    res.append(top.val)
                tn = top.right
        return res