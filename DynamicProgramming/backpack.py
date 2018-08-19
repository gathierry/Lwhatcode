'''
dp[s][i] 表示“前i”个物品，取出一些能否组成和为s

dp[s][i] = dp[s][i-1] || dp[s-a[i]][i-1]

  i  0  1  2  ...  n
s
0    T  T  T  ...  T (全部选择不取)
1    F
2    F
...
m    F

'''

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        res = 0
        dp = [True] + [False for i in range(m)]  # len = m+1
        for i in range(0, n):
            for s in range(m, 0, -1):  # m, m-1, ..., 1
                if s-A[i] >= 0:
                    dp[s] = dp[s] | dp[s-A[i]]
                else:
                    dp[s] = dp[s]
                if dp[s]:
                    res = max(s, res)
                    if s == m:
                        return res
        return res

if __name__ == '__main__':
    s = Solution()
    A = [2, 3, 5, 7]
    m = 11
    print(s.backPack(m, A))
                    
        