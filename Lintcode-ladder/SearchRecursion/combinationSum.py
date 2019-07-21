'''
取其中一个数 n，则下一步要递归的是 target-n

先选 x0, 之后在相同范围内继续选，但 target-x0, 
之后为了不重复，从 x1 开始


'''



class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        result = []
        self.f(candidates, target, [], result)
        return result
        
        
    def f(self, candidates, target, current, result):
        '''
        @param candidates: A list of integers
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
        idx = 0
        tmp = candidates[0] - 1
        while idx < len(candidates):
            v = candidates[idx]
            if tmp != v:
                self.f(candidates[idx:], target, current+[v], result)
                tmp = v
            idx += 1
    
if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum([2,3,6,7], 7)
    print(res)
        
        
