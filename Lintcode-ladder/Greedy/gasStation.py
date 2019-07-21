'''
1. 如果总的gas - cost小于零的话，那么没有解返回-1
2. 如果前面所有的gas - cost加起来小于零，那么前面所有的点都不能作为出发点。
解释： s0  s1  s2  s3
        c0  c1  c2  c3
     如果可以从 s0 到 s2，说明 s0 - c0 + s1 - c1 >= 0
                         且 s0 - c0 >= 0
     如果此时发现 s2 不能到 s3，则说明 s0 + s1 +s2 - c0 - c1 - c2 = s1 + s2 - c1 - c2 + (s0 - c0)< 0
     那么如果是从 s1 出发则一定也不能到 s3，因为 s1 + s2 - c1 - c2 < 0

由此可知，如果发现 s0 到 sk 不可到达，就可以直接从 s_k+1 开始试了
'''


class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if sum(cost) > sum(gas):
            return -1
        start = 0
        while start < len(gas):
            success, idx = self.goFrom(gas, cost, start)
            if success:
                return idx
            else:
                start = idx
        return -1
            
                    
    def goFrom(self, gas, cost, start):
        g = 0
        i = start
        while g >= 0:
            g += gas[i]
            g -= cost[i]
            i += 1
            if i == len(gas):
                return True, start
        return False, i
        
if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([1,1,3,1], [2,2,1,1]))
            
            
