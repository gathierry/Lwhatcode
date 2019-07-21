"""
Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

Challenge
o(n) time and O(k) memory
"""

"""
这道题在商汤面试时遇到过
使用队列存储 [a0, a1, ...]
如果 a1 大于 a0，则用 a1 替换 a0，否则 a1 放在 a0 后面
弹出时，如果 nums 要弹出的值与队首值相同，就一起弹出
"""



class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        res = []
        queue = []
        if len(nums) == 0:
            return []
        if len(nums) <= k:
            return [max(nums)]
        for i, num in enumerate(nums):
            if len(queue) == 0:
                queue.append(num)
            else:
                while len(queue) > 0 and num > queue[-1]:
                    queue.pop()
                queue.append(num)
            if i >= k-1:
                res.append(queue[0])
                if nums[i+1-k] == queue[0]:
                    queue.pop(0)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1,2,7,7,8], 1))
    
            
