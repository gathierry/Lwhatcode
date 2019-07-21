'''
采用贪心法即可，譬如[2, 3, 1, 1, 4]
每次跳跃1步，我们可跳跃步数减1，如果新的位置步数大于剩余步数，使用新的步数继续移动，如果可跳跃次数小于0并且还没到最后一个元素，那么失败。
时间复杂度 O(n)
'''

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if len(A) <= 1:
            return True
        i = 0
        reach = 0  # furthest index can be reach
        while i < len(A) - 1 and reach >= i:
            reach = max(A[i] + i, reach)
            if reach >= len(A) - 1:
                return True
            i += 1
        return False
            
            
            
            
        
if __name__ == '__main__':
    s = Solution()
    #print(s.canJump([2,3,1,1,4]))
    #print(s.canJump([3,2,1,0,4,1]))
    print(s.canJump([0]))
    