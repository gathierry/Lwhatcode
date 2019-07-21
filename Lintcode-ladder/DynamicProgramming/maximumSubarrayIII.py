"""
dp_local[j][i] 前i个元素k=j时的结果，必须包含 i
dp_global[j][i] 前i个元素k=j时的结果，不必须包含 i
dp_local[j][i] = max(dp_global[j-1][i-1], dp_local[j][i-1]) + nums[i]
dp_global[j][i] = max(dp_local[j][i], dp_global[j][i-1])
参考：https://zhengyang2015.gitbooks.io/lintcode/maximum_subarray_iii_43.html
"""

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        dp_local = []
        dp_global = []
        col1 = []
        s = 0
        max_tmp = -float('inf')
        for num in nums:
            if len(dp_global) == 0:
                dp_local.append(num)
                dp_global.append(num)
            else:
                ele = max(dp_local[-1]+num, num)
                dp_local.append(ele)
                max_tmp = max(max_tmp, ele)
                dp_global.append(max_tmp)
            s += num
            col1.append(s)
        for j in range(2, k+1):
            for i in range(j, len(nums)):
                dp_local[i] = max(dp_global[i-1], dp_local[i-1]) + nums[i]
            dp_global[j-1] = col1[j-1]
            for i in range(j, len(nums)):    
                dp_global[i] = max(dp_global[i-1], dp_local[i])
        return dp_global[-1]
    
if __name__ == '__main__':
    s = Solution()
    nums = [-1,4,-2,3,-2,3]
    k = 2
    nums = [-1,-2,-3,-100,-1,-50]
    nums = [-1, 0, 1]
    k = 3
    nums = [-42,81,-43,97,-82,20,-33,49,-62,2,-43,18,-54,52,-29,31,-70,87,-75,47,-22,42,-56,97,-100,54,-33,14,-89,34,-81,60,-66,75,-99,91,-93,70,-10,30,-26,72,-95,66,-41,23,-23,31,-14,78,-74,92,-20,25,-57,41,-72,58,-46,44,-52,53,-85,73,-37,96,-91,85,-77,62,-9,73,-64,63,-12,18,-61,24,-75,95,-54,89,-61,63,-19,24,-46,87,-87,69,-98,26,-92,26,-70,40,-63,20,-10,18,-64,26,-23,84,-35,65,-81,26,-55,92,-72,15,-99,18,-84,95,-50,77,-44,20,-20,94,-98,62,-67,17,-23,23,-75,33,-90,1,-1,86,-31,96,-80,100,-65,93,-51,48,-47,81,-63,100,-84,3,-15,59,-53,99,-67,12,-94,24,-98,74,-24,4,-34,79,-19,35,-54,36,-42,60,-68,18,-62,12,-50,44,-22,61,-21,27,-14,48,0,78,-39,70,-46,1,-86,77,-98,55,-93,81,-70,48,-3,0,-46,71,-50,11]
    k = 2
    print(s.maxSubArray(nums, k))