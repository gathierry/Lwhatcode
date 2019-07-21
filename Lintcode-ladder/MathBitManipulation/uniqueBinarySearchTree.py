'''
这道题实际上是 Catalan Number 卡塔兰数的一个例子。

对于 1, 2, 3, ..., n 数列，结果是以 1 为根的树 + 以 2 为根的树 + ...
对于以 1 为根的树，左子树有 0 个元素，右子树有 n-1 个元素，有可能的组合数就是 dp[0] * dp[n-1] (每种左子树都可以与任意一种右子树组合成新树)
对于以 2 为根的树，左子树有 1 个元素，右子树有 n-2 个元素，有可能的组合数就是 dp[1] * dp[n-2]

所以就有了卡特兰数列的递推式：

C_{n+1} = \sum_{i=0}^n C_i C_{n-i}
C_0 = 1 (空树)
'''



class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    # recursive
    def numTrees2(self, n):
        # write your code here
        if n == 0:
            return 1
        s = 0
        for i in range(n):
            s = s + self.numTrees(i) * self.numTrees(n-1-i)
        return s
    
    # loop
    def numTrees(self, n):
        dp = [1]
        for i in range(1, n+1):
            dp_tmp = 0
            for j in range(i):
                dp_tmp += dp[j] * dp[i-1-j]
            dp.append(dp_tmp)
        return dp[n]
        

        
if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
