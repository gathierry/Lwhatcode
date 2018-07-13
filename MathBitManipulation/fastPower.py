'''
取模运算乘法法则 (a * b) % p = (a % p * b % p) % p

a^n % b = (a^(n/2) % b * a(n/2) % b) % b   ------ n even
or 
((a^(n/2) % b * a(n/2) % b) % b * a % b) % b ---- n odd
'''

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        demi = self.fastPower(a, b, n//2)
        res = (demi % b * demi % b) % b
        if n % 2 == 1:
            res = (res * a % b) % b
        return res
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.fastPower(2, 3, 31))
    print(solution.fastPower(100, 1000, 1000))
        
        
        
