class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if len(nums) <= 1:
            return len(nums)
        i = 0
        j = 1
        
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        print(nums)
        return i+1
        
        
if __name__ == '__main__':
    solution = Solution()
    A = [1,1,2,2,3]
    print(solution.removeDuplicates(A))
                
