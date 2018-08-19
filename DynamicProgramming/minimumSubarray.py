'''
s > 0, s = min(s, num)
s <= 0, s = min(s, s+num)
'''

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        s = float('inf')
        for num in nums:
            if s > 0:
                s = min(s, num)
            else:
                s = min(s, s+num)
        return s
        
if __name__ == "__main__":
    s = Solution()
    print(s.minSubArray([1,-1,-2,1]))
    print(s.minSubArray([1,1]))
    print(s.minSubArray([-5,10,-4]))