'''
2x5会使末尾产生 0
质因数分解后而 2 的个数一定大于 5 的个数
所以统计 5 的个数即可
例如 11 要统计 11！中会分解出几个 5，可以用 11//5 
但是如果是 25 则多出一个 0，所以对于 //25 要再加一个 0
以此类推 125 再加一个 0
'''

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        res = 0
        num = 5
        while n >= num:
            res += n // num
            num *= 5
        return res
            
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeros(21))