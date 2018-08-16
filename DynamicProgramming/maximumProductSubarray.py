'''
记录当前最大值 p[i] 和最小值 q[i]
当到第 k 个数时，最大值一定在 p[:i-1]*nums[k], q[:i-1]*nums[k], nums[k] 中产生
'''



class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        p = nums[0]
        q = nums[0]
        res = nums[0]
        for num in nums[1:]:
            tri = [p * num, q * num, num]
            p = max(tri)
            q = min(tri)
            res = max(p, res)
        return res
            
        
if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, -2, 4]
    nums = [-3, 0, 1, -2]
    s.maxProduct(nums)