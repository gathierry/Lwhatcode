'''
考虑时间和空间复杂度都为 O(mxn) 的解法
对于字符串 s t
令 L[i, j] 表示以 s[i] t[j] 结尾的相同子串的最大长度
则可以推出 L[i+1, j+1] = (s[i]==t[j]) * (L[i,j] + 1)
由此通过一个二维 list L 就可以求出想要的解
'''

from pprint import pprint

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if len(A) * len(B) == 0:
            return 0
        # init empty 2D list
        L = []
        for _ in range(len(A)):
            row = []
            for _ in range(len(B)):
                row.append(0)
            L.append(row)
        max_value = 0
        # init first row and first column
        for i in range(len(A)):
            if A[i] == B[0]:
                L[i][0] = 1
                max_value = 1
        for j in range(len(B)):
            if A[0] == B[j]:
                L[0][j] = 1
                max_value = 1
        if max(len(A), len(B)) > 1:
            for i in range(1, len(A)):
                for j in range(1, len(B)):
                    L[i][j] = (L[i-1][j-1] + 1) * int(A[i]==B[j])
                    max_value = max(L[i][j], max_value)
        return max_value
        
        
        
        
if __name__ == '__main__':
    solution = Solution()
    
    A = "www.lintcode.com code"
    B = "www.ninechapter.com code"
    print(solution.longestCommonSubstring(A, B))