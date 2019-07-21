'''
这道题依然是依靠 xor 操作。
但是因为有两个单独数 a, b，所以
第一步，将数列分为两组，每组只包含一个单独数
    先对所有数做 xor
    得到的数是 s = a ^ b 其中 0 表示两数相同的位，1 表示两数不同的位
    那么找到有 1 的一位
        x = s & -s （反码+1） 可以找到最右的 1, 其余位变成 0
    所有数和 x 做 & 运算，为 0 的一组，不为 0 的一组
第二步，分别做xor
'''
class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        s = 0
        for a in A:
            s ^= a
        n = s & -s
        print(bin(n))
        s1 = 0
        s2 = 0
        for a in A:
            m = a & n
            if m > 0:
                s1 ^= a
            else:
                s2 ^= a
        return [s1, s2]
                
if __name__ == '__main__':
    s = Solution()
    #print(s.singleNumberIII([1,2,2,3,4,4,5,3]))
    print(s.singleNumberIII([1,5,-1,1,2,2,3,4,4,5,3,2147483647,8,9,9,8]))