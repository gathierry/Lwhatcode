'''
如果是 2 项，结果是 [a, b], [b, a]
如果是 3 项，结果是 [a, [b, c]], [a, [c, b]], 
                 [b, [a, c]], [b, [c, a]], 
                 [c, [a, b]], [c, [b, a]]
'''

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            ps = self.permute(nums[:i]+nums[i+1:])
            for p in ps:
                res.append([nums[i]] + p)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))