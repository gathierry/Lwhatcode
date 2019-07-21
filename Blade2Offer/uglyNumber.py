"""
Write a program to check whether a given number is an ugly number`.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Example
Given num = 8 return true
Given num = 14 return false

Notice
Note that 1 is typically treated as an ugly number.
"""

"""
判断a是b的质因数的办法是看b % a==0
解法一：
逐个整除之前的数判断
解法二：
不断除 2，3，5
解法二：
从小到大枚举丑数，超过 num 时即可确定
queue1: 1x2 2x2 3x2  ...
queue2: 1x3 2x3 3x3  ...
queue3: 1x5 2x5 3x5  ...
"""

class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly2(self, num):
        # write your code here
        if num == 0:
            return False
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        return num==1
        
    def isUgly(self, num):
        # write your code here
        if num == 1:
            return True
        q2 = [2]
        q3 = [3]
        q5 = [5]
        res = 0
        while res < num:
            cur_min = min(q2[0], q3[0], q5[0])
            for q in [q2, q3, q5]:
                if q[0] == cur_min:
                    res = q.pop(0)
                    if res == num:
                        return True
            q2.append(cur_min*2)
            q3.append(cur_min*3)
            q5.append(cur_min*5)
        return False
    
if __name__ == '__main__':
    s = Solution()
    s.isUgly(8)
                    
                    
                    
                    
                    
        