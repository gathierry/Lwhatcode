'''
s[k] = s[k-1] + s[k-2]

'''

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n < 2:
            return n
        s = [0 for k in range(n)]
        s[0] = 1
        s[1] = 2
        for k in range(2, n):
            s[k] = s[k-1] + s[k-2]
        return s[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(1))
        