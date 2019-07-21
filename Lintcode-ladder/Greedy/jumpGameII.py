'''
在 i 时，i+A[i] 以内都可以一步到达

使用和 jump game 一样的方法不断更新能覆盖的最远点 reach
设定一个变量 last 作为当前能到的最远点，也就是在目前基础上能一步到达的最远点
每当要离开当前 last 覆盖范围的时候，用已知能达到的最远 reach 作为下一个 last，此时步数 +1
'''


class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        reach = 0  # furthest index can be reach
        last = 0
        step = 0
        for i in range(len(A)):
            if i > last:
                last = reach
                step += 1
            reach = max(A[i] + i, reach)
        return step
        
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,3,1,1,1]))
