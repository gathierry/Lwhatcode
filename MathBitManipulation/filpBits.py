'''
负数的二进制表示：绝对值取反加 1
例如： -5 （32位）
5：00000000 00000000 00000000 00000101
反 11111111 11111111 11111111 11111010
补 11111111 11111111 11111111 11111011
python 中可以用 bin(((1 << 32) - 1) & a) 表示 a 的二进制, a 可正可负
'''

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        stra = bin(((1 << 32) - 1) & a)[2:]
        strb = bin(((1 << 32) - 1) & b)[2:]
        c = 0
        ia = len(stra) - 1
        ib = len(strb) - 1
        while ia >= 0 and ib >= 0:
            if stra[ia] != strb[ib]:
                c += 1
            ia -= 1
            ib -= 1
        if ia >= 0:
            for s in stra[:ia+1]:
                if s=='1':
                    c += 1
        if ib >= 0:
            for s in strb[:ib+1]:
                if s=='1':
                    c += 1
        return c
        
        
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.bitSwapRequired(31, 14))
    print(solution.bitSwapRequired(1, -2))