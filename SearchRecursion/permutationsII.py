

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        return self.p(nums)
        
        
    def p(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ps = self.p(nums[:i]+nums[i+1:])
            for p in ps:
                res.append([nums[i]] + p)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,2,2]))