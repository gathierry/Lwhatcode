'''
同 majority number ii 类似，这次空间复杂度上的要求是 O(k)
那么可以准备 k-1 个 counter，遇到新的就集体 -1
'''


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        d = {}
        for n in nums:
            if n not in d:
                if len(d) < k - 1:  # if still have space
                    d[n] = 1
                    continue
                else:
                    k2rm = []
                    for key in d.keys():  # if no more space,  all -1, if zero, remove element
                        d[key] -= 1
                        if d[key] == 0:
                            k2rm.append(key)
                    for key in k2rm:
                        d.pop(key)
            else:
                d[n] += 1
        for key in d.keys():
            d[key] = 0
        for n in nums:
            if n in d:
                d[n] += 1
        return max(d, key=d.get)
            
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.majorityNumber([3,1,2,3,2,3,3,4,4,4], 3))
            
        
