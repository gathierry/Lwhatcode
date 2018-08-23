# -*- coding: utf-8 -*-
"""
解法一：
dp[i] = max({dp[j]+1, any j s.t. A[j] <= A[i]})
表示包含 A[i] 的最长递增子序列的长度
时间复杂度：O(n2)
解法二：
构建一个新的递增序列B，尽保证紧凑，即每一项与前一项间距尽量小
在B中选择插入点时，因为B是有序的，所以可以用二分法
时间复杂度：O(nlogn)
参考 https://blog.csdn.net/left_la/article/details/11951085
"""

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence1(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        dp = [1]
        for num in nums[1:]:
            maxV = 1
            for i, d in enumerate(dp):
                if nums[i] < num:
                    maxV = max(maxV, d+1)
            dp.append(maxV)
        print(dp)
        return max(dp)
    
    def replaceInB(self, B, num, lb, rb):
        if lb == rb:
            B[lb] = num
            return
        mid = (lb + rb) // 2
        if num > B[mid]:
            self.replaceInB(B, num, mid+1, rb)
        else:
            self.replaceInB(B, num, lb, mid)
    
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        B = [nums[0]]
        for num in nums[1:]:
            if num > B[-1]:
                B.append(num)
            else:
                self.replaceInB(B, num, 0, len(B)-1)
        return len(B)
                
    
if __name__ == '__main__':
    s = Solution()
    nums1 = [5, 4, 1, 2, 3]
    nums2 = [4, 2, 4, 5, 3, 7]
    nums3 = [88,4,24,82,86,1,56,74,71,9,8,18,26,53,77,87,60,27,69,17,76,23,67,14,98,13,10,83,20,43,39,29,92,31,0,30,90,70,37,59]
    print(s.longestIncreasingSubsequence(nums1))  #3
    print(s.longestIncreasingSubsequence(nums2))  #4
    print(s.longestIncreasingSubsequence(nums3))  #10
                    
