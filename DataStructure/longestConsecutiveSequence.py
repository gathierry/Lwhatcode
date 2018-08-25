'''
将所有元素放进set
取出一个，找前后相邻项，直到找不到为止
'''

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        nums = set(num)
        res = 0
        for n in num:
            if n in nums:
                tmp = 1
                nums.remove(n)
                k = n - 1
                while k in nums:
                    tmp += 1
                    nums.remove(k)
                    k = k - 1
                k = n + 1
                while k in nums:
                    tmp += 1
                    nums.remove(k)
                    k = k + 1
            res = max(tmp, res)
        return res
        
if __name__ == '__main__':
    s = Solution()
    num = [0,0,-1]
    print(s.longestConsecutive(num))