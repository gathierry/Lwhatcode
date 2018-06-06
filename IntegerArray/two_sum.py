'''
解法一：
先排序，之后两个指针分别从头、尾向中间推
空间复杂度 O(n)，时间复杂度 O(nlogn)

解法二：
构建一个 Hashmap, key: number in list, value: index
用 target - number，再找差
空间复杂度 O(n)，时间复杂度 O(n)

下面实现第二种解法
'''


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        d = {}
        for i, n in enumerate(numbers):
            if n not in d:
                d[n] = []
            d[n].append(i)
        result = []
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in d:
                if len(d[diff]) == 1:
                    result = [i, d[diff][0]]
                else: # repeated number. this is the only choice because the solution is unique
                    result = d[diff]
                break
        result.sort()
        return result

if __name__ == '__main__':
    solution = Solution()
    numbers=[2, 7, 11, 15]
    target=9
    print(solution.twoSum(numbers, target))
        
        