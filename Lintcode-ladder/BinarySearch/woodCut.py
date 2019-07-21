'''
这道题可以用二分法
能取得的最大长度，是 max(L)，最短是 1，所以在这中间查找
因为 solution.woodCut([232], 1) 时会取不到上界，所以让上界 = 最大能取到的值+1
'''


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if len(L) == 0:
            return 0
        l_max = max(L)
        lb = 1
        ub = l_max + 1
        while lb + 1 < ub:
            m = (lb + ub) // 2
            n_piece = sum([l // m for l in L])
            if n_piece >= k:
                lb = m
            elif n_piece < k:
                ub = m
        n_piece = sum([l // lb for l in L])
        if n_piece >= k:
            return lb
        return 0



if __name__ == '__main__':
    solution = Solution()
    print(solution.woodCut([232, 124, 456], 7))
    print(solution.woodCut([2147483644,2147483645,2147483646,2147483647], 4))
    print(solution.woodCut([232], 1))
