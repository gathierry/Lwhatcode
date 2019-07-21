'''
这道题可以转换成图搜索，任意两个只有一个字母区别的词都是相邻的
无向无权图最短路用 bfs，因为广度优先搜索最先访问到的是相邻的点，所以距离最近的点最先访问到，记录的距离也就最小。时间复杂度 O(V+E)
参考 https://www.cnblogs.com/zuoyuan/p/3765858.html
'''


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = []
        queue.append((start, 1))
        while queue:
            currword, currlen = queue.pop(0)
            if currword == end:
                return currlen
            for i in range(len(currword)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = currword[:i] + j + currword[i+1:]
                        if nextword in dict:
                            queue.append((nextword, currlen+1))
                            dict.remove(nextword)
        return 0
        
if __name__ == '__main__':
    s = Solution()
    start = "hit"
    end = "cog"
    dict = set(["hot", "dot", "dog", "lot", "log"])
    print(s.ladderLength(start, end, dict))