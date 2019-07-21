'''
参考 http://www.cnblogs.com/grandyang/p/4743837.html

(1) 1x2,  2x2, 3x2, nx2, ...
(2) 1x3,  2x3, 3x3, nx3, ...
(3) 1x5,  2x5, 3x5, nx5, ...
三个队列，分别是2，3，5乘以ugly number
对比后哪个小就弹出哪个，而生成的 ugly number 就作为新的数分别进入三个队列
'''

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n == 1:
            return 1
        l1 = [2]
        l2 = [3]
        l3 = [5]
        res = 1
        for i in range(n-1):
            res = min(l1[0], l2[0], l3[0])
            for l in [l1, l2, l3]:
                if res == l[0]:
                    l.pop(0)
            l1.append(2*res)
            l2.append(3*res)
            l3.append(5*res)
        return res
            


