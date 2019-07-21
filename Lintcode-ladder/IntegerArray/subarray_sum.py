'''
计算每个从头开始到 i 的和，如果出现和为 0 或者和有重复时，可以结束
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        d = {}  # sum: index
        s = 0
        for i, n in enumerate(nums):
            s += n
            if s == 0:
                return [0, i]
            if s not in d:
                d[s] = i
            else:
                return [d[s]+1, i]
        
if __name__ == '__main__':
    solution = Solution()
    A = [-3, 2, 3, -5, 4]
    print(solution.subarraySum(A))
    