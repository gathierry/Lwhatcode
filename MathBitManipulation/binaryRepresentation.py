'''
整数部分和小数部分分开处理
整数部分：a 除以 2 取余数，从右向左填充，直到 a 被除成 0
小数部分：a 乘以 2 取整数部分，从左向右填充，剩余小数部分再乘以 2，直到小数部分为 0 (https://www.cnblogs.com/upzone/articles/1389365.html)

'''


class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binaryRepresentation(self, n):
        # write your code here
        a2 = ''
        b2 = ''
        a, b = n.split('.')
        
        if a == '0':
            a2 = '0'
        a = int(a)
        while a != 0:
            a2 = str(a%2) + a2
            a //= 2
            
        if int(b) == '0' or b == '':
            b2 = ''
        b = float('0.' + b)
        while b != 0:
            b *= 2
            b2 += str(int(b))
            b -= int(b)
            if len(b2) > 32:
                return 'ERROR'
            
        res = a2 + '.' + b2
        while res[-1] == '0':
            res = res[:-1]
        if res[-1] == '.':
            res = res[:-1]
            
        return res
            
            
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.binaryRepresentation('1.0'))
    print(solution.binaryRepresentation('3.5'))
    print(solution.binaryRepresentation('3.72'))
    print(solution.binaryRepresentation("17817287.6418609619140625"))