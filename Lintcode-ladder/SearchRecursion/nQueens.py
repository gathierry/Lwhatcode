'''
皇后问题有个技巧的关键在于棋盘的表示方法，这里使用一个数组就可以表达了。
比如board=[1, 3, 0, 2]，这是4皇后问题的一个解，
意思是：在第0行，皇后放在第1列；在第1行，皇后放在第3列；在第2行，皇后放在第0列；在第3行，皇后放在第2列。

判断斜向冲突可以用 abs(col_diff) == abs(row_diff)

思路是 dfs
'''


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        queue = []
        board = []
        res = [None for k in range(n)]
        for k in range(n):
            queue.append([0, k])
        while queue:
            v = queue.pop()
            for k in range(v[0], n):
                res[k] = None 
            res[v[0]] = v[1]
            row = v[0] + 1
            if row == n:
                board.append([x for x in res])
                continue
            for k in range(n):
                keep_flag = True
                for r, c in enumerate(res):
                    if c is None:
                        continue
                    if c == k or abs(r-row) == abs(c-k):
                        keep_flag = False
                        break
                if keep_flag:
                    queue.append([row, k])
        return self.index2code(board)
        
    def index2code(self, board):
        if len(board) == 0:
            return []
        res = []
        l = len(board[0])
        for b in board:  # b = [2, 0, 3, 1]
            blank = []
            for bb in b:
                line = ['.' for k in range(l)]
                line[bb] = 'Q'
                blank.append(''.join(line))
            res.append(blank)
        return res
            
        
if __name__ == '__main__':
    from pprint import pprint
    s = Solution()
    pprint(s.solveNQueens(4))
        
        
