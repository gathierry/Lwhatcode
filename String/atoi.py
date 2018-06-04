'''
检查字符串是否为空
对非法输入，返回0，并设置全局变量
溢出
空字符串 ""
输入字符串只有"+"或"-"号
'''

class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # write your code here
        if str == '':
            return 0
        # spaces at start
        i = 0
        while str[i] == ' ':
            i += 1
        # sign
        sign = 1
        if str[i] == '-':
            i += 1
            sign = -1
        if str[i] == '+':
            i += 1
        
        num = 0
        while i < len(str):
            if str[i] == '.':
                break
            if str[i] > '9' or str[i] < '0':
                return 0
            digit = ord(str[i]) - ord('0')
            num = 10 * num + digit
            i += 1
        if sign == 1 and num > 2147483647:
            return 2147483647
        if sign == -1 and num > 2147483648:
            return -2147483648
        return sign * num
            
            
if __name__ == '__main__':
    solution = Solution()
    
    print(solution.atoi('10'))
    print(solution.atoi('-1'))
    print(solution.atoi('123123123123123'))
    print(solution.atoi('1.0'))