'''
递归做法：DFS
对于 [1,2,3]
可以看做 不能重复）
[]
    1
        12
            123
        13
    2
        23
    3

非递归做法：https://blog.csdn.net/u013140542/article/details/38457093
0 - n 位，每一位取 0 或 1
当 第 n 位取到 1 时说明都取过了

'''



class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, current, res):
        """
        在 current 的基础上接一个子集
        子集第一位从 start 开始
        """
        res.append(current)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i+1, current+[nums[i]], res)
            
if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))