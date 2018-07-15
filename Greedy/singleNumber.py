'''
Challenge: One-pass, constant extra space.
利用XOR运算，原文地址:https://oj.leetcode.com/discuss/6170/my-o-n-solution-using-xor
因为A XOR A = 0，且 XOR 运算是可交换的，于是，对于实例 {2,1,4,5,2,4,1} 就会有这样的结果：
(2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5
'''


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        res = 0
        for a in A:
            res ^= a
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,3,4,3,4,1,2,5]))