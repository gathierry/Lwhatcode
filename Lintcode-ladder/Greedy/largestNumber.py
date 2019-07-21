'''
可以换一下思路，要想比较两个数在最终结果中的先后位置，何不直接比较一下不同组合的结果大小？
举个例子：要比较3和34的先后位置，可以比较334和343的大小，而343比334大，所以34应当在前
这种比较方法也是具有传递性的，即 a > b, b > c => a > c
'''

import functools

def concat_cmp(a, b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    if ab > ba:
        return -1
    elif ab == ba:
        return 0
    else:
        return 1


class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        nums.sort(key=functools.cmp_to_key(concat_cmp))
        res = ''
        for n in nums:
            res += str(n)
        return str(int(res))
        
if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([1, 20, 23, 8, 4]))
        
        
        
