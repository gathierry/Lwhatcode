'''
每到一个 x_k 选择是抛弃之前的，只保留 x_k 还是用之前累计的+x_k
这样可以覆盖所有可能结果
在这些中取最小值
'''

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        res = nums[0]
        dp = nums[0]
        for num in nums[1:]:
            dp = min(num, dp+num)
            res = min(res, dp)
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, -1, -2, 1]
    nums = [-5, 10, -4]
    print(s.minSubArray(nums))