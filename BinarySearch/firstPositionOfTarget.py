'''
仍然用二分法，但是这次要注意相同元素可能重复多次，处理 A[mid]=target 相等时和以往不同 
'''

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        ub = len(nums) - 1
        lb = 0
        while lb < ub:
            m = (lb + ub) // 2
            if target > nums[m]:
                lb = m + 1
            elif target < nums[m]:
                ub = m - 1
            else:
                ub = m
        if nums[lb] == target:
            return lb
        else:
            return -1




if __name__ == '__main__':
    solution = Solution()
    print(solution.binarySearch([1,2], 2))
    print(solution.binarySearch([1, 2, 3, 3, 4, 5, 10], 7))