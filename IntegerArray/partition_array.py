'''
依然用夹逼法。注意分析靠近时的各种情况。
可以分析当i，j之间还隔一个时的四种情况及后续
| i | | j |:
|>=k| | <k|
|>=k| |>=k|
| <k| | <k|
| <k| |>=k|
'''

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while i <= j:  # must contain equal
            if nums[i] >= k and nums[j] < k:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] >= k and nums[j] >= k:
                j -= 1
            elif nums[i] < k and nums[j] < k:
                i += 1
            else:  # nums[i] < k and nums[j] >= k
                i += 1
                j -= 1
        
        return i
        
if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,2,3]
    k = 3
    print(solution.partitionArray(nums, k))
    
    nums = [7,7,9,8,6,6,8,7,9,8,6,6]
    k = 10
    
    
    nums = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
    k = 9
    print(solution.partitionArray(nums, k))