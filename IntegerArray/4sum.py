from pprint import pprint


# 方法一
class Solution1:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        m = {}
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                s = numbers[i] + numbers[j]
                if s not in m:
                    m[s] = []
                m[s].append([i, j])
        pprint(m)
        # build pairs
        pairs = []
        for k in m.keys():
            if target - k in m.keys():
                pairs.append([k, target - k])
        print(pairs)
        results = []
        for p1, p2 in pairs:
            if p1 == p2:
                for i in range(len(m[p1])):
                    for j in range(i+1, len(m[p1])):
                        idcs = m[p1][i] + m[p1][j]
                        if len(set(idcs)) == 4:
                            r = [numbers[idx] for idx in idcs]
                            r.sort()
                            if r not in results:
                                results.append(r)
            else:
                for i in range(len(m[p1])):
                    for j in range(len(m[p2])):
                        idcs = m[p1][i] + m[p2][j]
                        if len(set(idcs)) == 4:
                            r = [numbers[idx] for idx in idcs]
                            r.sort()
                            if r not in results:
                                results.append(r)
        return results

# 方法二
class Solution2:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        numbers.sort()
        res = []
        length = len(numbers)
        for i in range(0, length - 3):
            if i and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                sum = target - numbers[i] - numbers[j]
                left, right = j + 1, length - 1
                while left < right:
                    if numbers[left] + numbers[right] == sum:
                        res.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        right -= 1
                        left += 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1
                    elif numbers[left] + numbers[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res



if __name__ == '__main__':
    solution = Solution2()
    numbers = [1, 0, -1, 0, -2, 2]
    target = 0
    numbers = [1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,0,0,-2,2,-5,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99]
    target = 11
    print(solution.fourSum(numbers, target))