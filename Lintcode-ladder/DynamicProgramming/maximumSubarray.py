'''
从头开始求 sum(0, k)
找出最大 index i 和最小index j
如果 i > j, 那么就是 i 到 j 之间
反之 i < j, 找到 j 后面的最大 index k，比较 j 到 k 和 0 到 i

动态规划解法
假设 dp[i] 是数组 a[0, i] 区间最大的值
dp[i + 1] = max(dp[i], dp[i] + a[i + 1])

使用分治算法，复杂度从 O(n) 降到 O(nlogn)
假设数组A[left, right]存在最大区间，mid = (left + right) / 2，那么无非就是三中情况：
1. 最大值在A[left, mid - 1]里面
2. 最大值在A[mid + 1, right]里面
3. 最大值跨过了mid，也就是我们需要计算[left, mid - 1]区间的最大值 + [mid + 1, right]的最大值 + mid，三者之和就是总的最大值
'''

class Solution2:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        s = 0
        res = -float('inf')
        for n in nums:
            s += n
            res = max(res, s)
            if s < 0:
                s = 0  # discard
        return res
        
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        return self.divide(nums, 0, len(nums)-1)
        
    def divide(self, nums, left, right):
        if left > right:
            return -float('inf')
        mid = (left + right) // 2
        lmax = self.divide(nums, left, mid-1)
        rmax = self.divide(nums, mid+1, right)
        
        s = 0
        mlmax = 0
        for i in range(mid-1, left-1, -1):
            s += nums[i]
            mlmax = max(mlmax, s)
        s = 0
        mrmax = 0
        for i in range(mid+1, right+1):
            s += nums[i]
            mrmax = max(mrmax, s)
        return max([lmax, rmax, mlmax+nums[mid]+mrmax])
        
if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
            
    
            