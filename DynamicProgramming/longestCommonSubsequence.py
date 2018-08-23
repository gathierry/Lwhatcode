# -*- coding: utf-8 -*-
"""
dp[i][j] A[:i]和B[:j]的最长子序列

if A[i] == B[j]
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
else
    dp = dp[i-1][j-1] + 1

e.g.    A  B  C  D
     i  1  2  3  4
   j
E  1    0  0  0  0
A  2    1
C  3    1
B  4    1
"""

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if len(A) == 0 or len(B) == 0:
            return 0
        dp = [1 for x in range(len(A))]
        col1 = [1 for x in range(len(B))]
        for i in range(len(A)):
            if A[i] != B[0]:
                dp[i] = 0
            else:
                break
        for j in range(len(B)):
            if A[0] != B[j]:
                col1[j] = 0
            else:
                break
        for j in range(1, len(B)):
            dp_tmp = [x for x in dp]
            dp_tmp[0] = col1[j]
            for i in range(1, len(A)):
                if A[i]==B[j]:
                    dp_tmp[i] = dp[i-1] + 1
                else:
                    dp_tmp[i] = max(dp[i], dp_tmp[i-1])
            dp = [x for x in dp_tmp]
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    A = "bedaacbade"
    B = "dccaeedbeb"
    print(s.longestCommonSubsequence(A, B))