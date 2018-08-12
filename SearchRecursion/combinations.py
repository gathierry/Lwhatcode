'''
采用递归的方式，在n个数中选k个，如果n大于k，那么可以分类讨论，如果选了n，那么就是在1到(n-1)中选(k-1)个，否则就是在1到(n-1)中选k个。
递归终止的条件是k为1，这时候1到n都符合要求。
'''

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if k == 1:
            return [[i + 1] for i in range(n)]
        result = []
        if n > k:
            result = [r + [n] for r in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
        else:
            result = [r + [n] for r in self.combine(n - 1, k - 1)]
        return sort(result)  # sort this for AC
        
        
if __name__ == '__main__':
    from pprint import pprint
    s = Solution()
    n = 13
    k = 3
    print(len(s.combine(n, k)))
    print(13*12*11/6)