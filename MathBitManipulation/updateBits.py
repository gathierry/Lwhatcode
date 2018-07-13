'''
需要生成一个 mask: 111111...1000001...1111, 从 i 到 j 位为 0，剩下为 1
100000 - 100 = 011100
参考 https://www.jianshu.com/p/e8a1f04190cf
'''

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        # write your code here
        n = ((1 << 32) - 1) & n
        m = ((1 << 32) - 1) & m
        m = m << i
        mask  = ~((1 << (j+1)) - (1 << i))
        return (n & mask) + m
        
        

if __name__ == '__main__':
    solution = Solution()
    #print(solution.updateBits(1024, 21, 2, 6))
    print(solution.updateBits(1, -1, 0, 31))