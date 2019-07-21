"""
Description
Given a unsorted array with integers, find the median of it.
A median is the middle number of the array after it is sorted.
If there are even numbers in the array, return the N/2-th number after sorted.

Example
Given [4, 5, 1, 2, 3], return 3.
Given [7, 9, 4, 5], return 5.

Challenge
O(n) time.
"""
"""
最简单的算法自然是先排序，再取中位数。
但是为了降低复杂度，可以借用快排的 partition 算法，每次只对相关的一侧做操作

另一个解法是构建一个最小堆，堆的大小是 n/2+1
"""

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        return self.getKthValue(nums, (len(nums)-1)//2)
        
    def partition(self, nums):
        pivot = nums[-1]
        left = 0
        right = len(nums) - 1
        storeIdx = left
        for i in range(right):
            if nums[i] < pivot:
                nums[i], nums[storeIdx] = nums[storeIdx], nums[i]
                storeIdx += 1
        nums[right], nums[storeIdx] = nums[storeIdx], nums[right]
        return storeIdx
        
    def getKthValue(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        storeIdx = self.partition(nums)
        if storeIdx == k:
            return nums[k]
        if storeIdx < k:
            return self.getKthValue(nums[storeIdx+1:], k-storeIdx-1)
        else:
            return self.getKthValue(nums[:storeIdx], k)

        
if __name__ == '__main__':
    s = Solution()
    print(s.median([4, 5, 1, 2, 3]))
    print(s.median([7, 9, 4, 5]))