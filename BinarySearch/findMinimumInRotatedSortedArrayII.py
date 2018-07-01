'''
这道题的输入可能有 duplicates
如果 nums[-1] < nums[0],说明最小值在中间
如果 nums[0] < nums[-1],说明最小值在 0
如果 nums[0] = nums[-1],则不好确定，考虑将右边界左移一位
'''

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        lb = 0
        ub = len(nums) - 1
        while nums[lb] >= nums[ub] and lb < ub:
            if nums[lb] == nums[ub]:
                ub -= 1
                continue
            m = (lb + ub) // 2
            if nums[m] > nums[ub]:
                lb = m + 1
            else:
                ub = m
        return nums[lb]
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin([1]))
    print(solution.findMin([4,4,5,6,7,0,0,1,2]))
    print(solution.findMin([1,1,-1,1]))