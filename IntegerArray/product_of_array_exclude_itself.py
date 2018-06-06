'''
[a1, a2, a3, ..., an]
构建两个数组
[1, a1, a1xa2, a1xa2xa3, ..., a1xa2x...xa(n-1)]
[a2x...xan, a3x...an, a4x...xan, ..., an, 1]
'''

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        B = list(range(1, len(nums)+1))
        p = 1
        for i in range(len(nums) - 1):
            p *= nums[i]
            B[i + 1] = p
        p = 1
        for i in range(len(nums)-1, 0, -1):
            p *= nums[i]
            B[i - 1] *= p
        return B
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.productExcludeItself([1, 2, 3, 4, 3, 2, 1]))