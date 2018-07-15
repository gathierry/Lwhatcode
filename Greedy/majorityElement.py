'''
Challenge: O(n) time and O(1) extra space
摩尔投票法 Moore Voting http://www.cnblogs.com/grandyang/p/4233501.html

先将第一个数字假设为众数，然后把计数器设为1，比较下一个数和此数是否相等，若相等则计数器加一，反之减一。
然后看此时计数器的值，若为零，则将当前值设为候选众数。
以此类推直到遍历完整个数组，当前候选众数即为该数组的众数。
'''


class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        mode = nums[0]
        count = 1
        for n in nums[1:]:
            if n == mode:
                count += 1
            else:
                if count == 1:
                    mode = n
        return mode
        
if __name__ == '__main__':
    s = Solution()
    print(s.majorityNumber([1, 1, 1, 1, 2, 2, 2]))