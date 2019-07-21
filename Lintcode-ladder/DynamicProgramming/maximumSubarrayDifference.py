'''
两次遍历，从左到右和从右到左。
用两个数组lmin[i],lmax[i]保存左侧到当前位置i的最大子数组和最小子数组的值，
再从右往左遍历找到右侧当前位置的最大子数组和最小子数组的值
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        lmin = [nums[0]]
        lmax = [nums[0]]
        cur_min = nums[0]
        cur_max = nums[0]
        for num in nums[1:]:
            cur_min = min(num, cur_min+num)
            lmin.append(min(lmin[-1], cur_min))
            cur_max = max(num, cur_max+num)
            lmax.append(max(lmax[-1], cur_max))
        
        rmin = [nums[-1]]
        rmax = [nums[-1]]
        cur_min = nums[-1]
        cur_max = nums[-1]
        for num in nums[-2::-1]:
            cur_min = min(num, cur_min+num)
            rmin.insert(0, min(rmin[0], cur_min))
            cur_max = max(num, cur_max+num)
            rmax.insert(0, max(rmax[0], cur_max))
        
        diff = -float('inf')
        for i in range(1, len(nums)):
            diff = max(diff, abs(lmin[i-1] - rmax[i]), abs(lmax[i-1] - rmin[i]))
        return diff
        
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, -3, 1]
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0]
    print(s.maxDiffSubArrays(nums))
        