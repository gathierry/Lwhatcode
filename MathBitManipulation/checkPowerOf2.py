class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n < 0:
            return False
        strn = bin(((1 << 32) - 1) & n)[2:]
        s = sum([int(s) for s in strn])
        print(strn)
        return s == 1
            
        
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPowerOf2(5))
    print(solution.checkPowerOf2(-2147483648))