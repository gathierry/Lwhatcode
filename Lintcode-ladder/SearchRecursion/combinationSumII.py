

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        result = []
        self.f(num, target, [], result)
        return result
        
    def f(self, num, target, current, result):
        '''
        @param num: A list of integers
        @param target: An integer
        @param current: Incomplete combination
        @param result: final result, list of combinations
        @return:
        '''
        s = sum(current)
        if s > target:
            return
        elif s == target:
            result.append(sorted(current))
            return
        if len(num) == 0:
            return
        idx = 0
        tmp = num[0] - 1
        while idx < len(num):
            v = num[idx]
            if tmp != v:
                self.f(num[idx+1:], target, current+[v], result)
                tmp = v
            idx += 1
            
if __name__ == '__main__':
    s = Solution()
    #res = s.combinationSum2([7,1,2,5,1,6,10], 8)
    res = s.combinationSum2([], 1)
    #res = s.combinationSum2([3,1,3,5,1,1], 8)
    print(res)