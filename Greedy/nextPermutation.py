'''
从右向左数到第一次出现 A[i] < A[i+1]
用 i 后面大于 A[i] 的最小一位替换 i
将第 i+1 位到最后排成递增

如果原数列单调递减，则说明已经是最大，把数列逆序即可
'''


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        l = len(nums)
        a = -1
        for i in range(l-1, 0, -1):
            if nums[i] > nums[i-1]:
                a = i
                break
        if a == -1:  # already maximum
            return nums[::-1]
        # sort from a to the end
        nums[a:] = sorted(nums[a:])
        for i in range(a, l):
            if nums[i] > nums[a-1]:
                nums[i], nums[a-1] = nums[a-1], nums[i]
                break
        return nums
        
            
            
        
            
if __name__ == '__main__':
    s = Solution()
    #print(s.nextPermutation([4,3,2,1]))
    #print(s.nextPermutation([1,3,2,3,1]))
    print(s.nextPermutation([1,3,2]))
