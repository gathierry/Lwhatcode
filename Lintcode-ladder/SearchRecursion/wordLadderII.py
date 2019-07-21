'''
与 wordladder 不一样，要打印所有符合要求的的结果
在 dict remove 的时候，要每个 level 结束后统一 remove，避免两条线中间有交点
比如
    start = "hit"
    end = "cow"
    dict = {"hit", "hot", "dot", "dog", "lot", "log", "cog", "cow"}
既然是一层一层处理，还是 bfs
'''

from pprint import pprint

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        preMap = {}
        for word in dict:
            preMap[word] = []
        currlevel = set()
        currlevel.add(start)
        while True:
            prelevel = currlevel.copy()
            currlevel = set()
            for word in prelevel:
                dict.remove(word)
            for word in prelevel:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = word[:i] + j + word[i+1:]
                            if nextword in dict:
                                preMap[word].append(nextword)
                                currlevel.add(nextword)
            if end in currlevel:
                break
        #pprint(preMap)
        res = []
        self.buildPath(preMap, start, [start], res, end)
        return res
        
    def buildPath(self, preMap, key, path, res, end):
        if key == end:
            res.append(path)
            return
        for word in preMap[key]:
            self.buildPath(preMap, word, path+[word], res, end)
        
        
        
if __name__ == '__main__':

    s = Solution()
    # start = "hit"
    # end = "cow"
    # dict = {"hit", "hot", "dot", "dog", "lot", "log", "cog", "cow"}
    # start = 'a'
    # end = 'c'
    # dict = {'a', 'b', 'c'}
    start = "hit"
    end = "cog"
    dict = {"hot","dot","dog","lot","log"}
    # start = "qa"
    # end = "sq"
    # dict = {"si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"}
    pprint(s.findLadders(start, end, dict))