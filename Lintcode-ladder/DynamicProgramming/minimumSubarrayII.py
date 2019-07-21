


class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        lmax = [nums[0]]
        cur_max = nums[0]
        for num in nums[1:]:
            cur_max = max(num, cur_max+num)
            lmax.append(max(lmax[-1], cur_max))

        rmax = [nums[-1]]
        cur_max = nums[-1]
        for num in nums[-2::-1]:
            cur_max = max(num, cur_max+num)
            rmax.insert(0, max(rmax[0], cur_max))

        res = -float('inf')
        for i in range(1, len(nums)):
            res = max(res, lmax[i-1]+rmax[i])
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, 2, -1, 2]
    print(s.maxTwoSubArrays(nums))