# -*- coding: utf-8 -*-
"""
dp[i][j] 表示在合法的情况下，第i个元素取值=j时的min cost

e.g [1    4    2  3], target=1
  i  1    2    3  4
j
1    0\
2    1-min+2
3    2/
4    3

"""

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        j_min = min(A)
        j_max = max(A)
        dp = [abs(A[0] - j) for j in range(j_min, j_max+1)]
        for a in A[1:]:
            dp_tmp = []
            for j_idx, j in enumerate(range(j_min, j_max+1)):
                cost = abs(a - j) + min(dp[max(0, j_idx-target):min(j_idx+target+1, j_max-j_min+1)])
                dp_tmp.append(cost)
            dp = [x for x in dp_tmp]
        return min(dp)
        
if __name__ == '__main__':
    s = Solution()
    #print(s.MinAdjustmentCost([1,4,2,3], 1))
    print(s.MinAdjustmentCost([11,11,3,5,11,16,12,11,15,11,16,16,16,16,16,11,16], 0))