'''
与 two sum 类似，在排序之后两个指针分别从头、尾向中间靠拢。因为要求三个数，所以先取出一个。
排序时间复杂度 O(nlogn), 左右遍历 O(n), 但因为每次取出了一个，所以是 O(n^2)
'''



class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        diff = float('inf')
        ss = 0
        for k, n in enumerate(numbers):
            i = k + 1
            j = len(numbers) - 1
            while i < j:
                s = n + numbers[i] + numbers[j]
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    return s
                if abs(target - s) < diff:
                    diff = abs(target - s)
                    ss = s
        return ss
        
if __name__ == '__main__':
    solution = Solution()
    numbers=[-1, 2, 1, -4]
    target=1
    #print(solution.threeSumClosest(numbers, target))
    
    numbers=[2,7,11,15]
    target=3
    print(solution.threeSumClosest(numbers, target))