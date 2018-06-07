'''
与 3 sum closest 相似
'''


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        numbers.sort()
        for k, n in enumerate(numbers):
            i = k + 1
            j = len(numbers) - 1
            while i < j:
                s = n + numbers[i] + numbers[j]
                if s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                else:
                    res.append((n, numbers[i], numbers[j]))
                    i += 1
                    j -= 1
        return list(set(res))
        
if __name__ == '__main__':
    solution = Solution()
    numbers=[-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(numbers))