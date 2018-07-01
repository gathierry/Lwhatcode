'''
对于 x，在 [0, x/2+1] 范围内搜索
'''

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x < 2:
            return x
        lb = 0
        ub = x // 2 + 1
        while lb < ub - 1:
            mid = (lb + ub) // 2
            if mid**2 > x:
                ub = mid
            else:
                lb = mid
            print(lb, ub)
        return lb
        


if __name__ == '__main__':
    solution = Solution()
    
    print(solution.sqrt(65536))
    