'''
dp[i][j] 表示  s[:i+j] 可以用 s1[:i] 和 s2[:j] 获得
dp[i][j] = (dp[i-1][j] + s1[i] == s3[i+j]) || (dp[i][j-1] + s2[j] == s3[i+j])

  i  0  1  2  ...  n
j    
0    T  
1
2
...
m                  x

'''

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [True] + [s1[:i]==s3[:i] for i in range(1, len(s1)+1)]
        for j in range(len(s2)):
            dp[0] = (s2[:j+1] == s3[:j+1])
            for i in range(1, len(s1) + 1):
                dp[i] = (dp[i-1] and s1[i-1]==s3[j+i]) or (dp[i] and s2[j]==s3[j+i])
        return dp[-1]
        
        
if __name__ == '__main__':
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # s3 = "aadbbbaccc"
    # s1 = ""
    # s2 = "a"
    # s3 = "a"
    s1 = "aacaac"
    s2 = "aacaaeaac"
    s3 = "aacaaeaaeaacaac"
    print(s.isInterleave(s1, s2, s3))