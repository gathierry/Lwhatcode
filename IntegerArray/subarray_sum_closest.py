'''
nums                -3  1  1 -3  5
sums              0 -3 -2 -1 -4  1 --sort--> -4 -3 -2 -1  0  1
sums_sorted_idcs  4  1  2  3  0  5
diffs                                            1  1  1  1  1  --min--> 1
                         get indices diff_idcs:  1  2  3  4  5
for e.g, take 1 (with 0), means in sum -3 and -4 is very close => [1 1 3] is a good subarray => should return [1, 3]
              2 (with 1)               -2     -3                  [1]                                         [1, 1]
...
'''

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        sums = [0]
        s = 0
        for n in nums:
            s += n
            sums.append(s)
        sums_sorted_idcs = sorted(range(len(sums)), key=lambda k: sums[k])
        sums.sort()
        
        min_value = float('inf')
        diff_idcs = []
        for i in range(1, len(sums)):
            diff = abs(sums[i] - sums[i-1])
            if diff < min_value:
                diff_idcs = [i]
                min_value = diff
            elif diff == min_value:
                diff_idcs.append(i)
                
        result = []
        for di in diff_idcs:
            a = sums_sorted_idcs[di-1]-1
            b = sums_sorted_idcs[di]-1
            l = min(a, b) + 1
            r = max(a, b)
            result.append([l, r])
        # 返回其中之一就好
        return result[0]
        
        
        
        
if __name__ == '__main__':
    solution = Solution()
    A = [-3, 1, 1, -3, 5]
    print(solution.subarraySumClosest(A))