'''
对二进制下每一位数 1 的个数，如果 %3 != 0 那么就是单独的数
计数为       0 -  1 -  2 -  0
转换成二进制 00 - 01 - 10 - 00
           xy
y = y ^ r & ~x
x = x ^ r & ~y

'''


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        x = 0
        y = 0
        for a in A:
            y = y ^ a & ~x
            x = x ^ a & ~y
        return y
        
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumberII([1,1,2,3,3,3,2,2,4,1]))
