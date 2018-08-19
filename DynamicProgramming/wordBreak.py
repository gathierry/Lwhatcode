'''
解法一：
dp[i] 表示s[:i+1] 是否在 dict 中
如果 dp[i-j] 是 且 dp[i-j:i+1] 是，那么 dp[i] 也是
但是这种解法要前查找，有多余计算

解法二：
向后查找，多余计算稍微少一点

'''

class Solution1:
    """
    这里的两个方法原理上一样，但是 wordBreak1 在 s 很长时会超时，wordBreak2 不会
    """
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak1(self, s, dict):
        # write your code here
        dp = [True] + [False for i in range(len(s))]  # first true as empty
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in dict:
                    dp[i+1] = True
                    break
        return dp[-1]
        
    def wordBreak2(self, s, dict):
        # write your code here
        dp = [True] + [False for i in range(len(s))]  # first true as empty
        for i in range(len(s)):
            for word in dict:
                l = len(word)
                if i + 1 >= l and s[i+1-l:i+1] == word and dp[i+1-l]:
                    dp[i+1] = True
                    break
        return dp[-1]
        
class Solution:
    """
    这里的两个方法原理上一样，但是 wordBreak1 在 s 很长时会超时，wordBreak2 不会
    """
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak1(self, s, dict):
        # write your code here
        dp = [True] + [False for i in range(len(s))]
        for i in range(len(s)):
            if dp[i]:
                for word in dict:
                    l = len(word)
                    if i+l <= len(s):
                        if s[i:i+l] == word:
                            dp[i+l] = True
        print(dp)
        return dp[-1]
        
    def wordBreak2(self, s, dict):
        # write your code here
        dp = [True] + [False for i in range(len(s))]
        for i in range(len(s)):
            if dp[i]:
                for j in range(1, len(s)-i+1):
                    if s[i:i+j] in dict:
                        dp[i+j] = True
        return dp[-1]
                
        
if __name__ == '__main__':
    solution = Solution()
    s = 'leetcode'
    dict = {'leet', 'code'}
    s = 'a'
    dict = {'a'}
    s = 'abcd'
    dict = {'a', 'b', 'abc', 'cd'}
    print(solution.wordBreak(s, dict))