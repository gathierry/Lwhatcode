'''
Eg. A = "178542", k = 4, answer is 12
先计算要保留的位数 l，然后从最左到 n-l 找最小 x
                      从 x-1 到 n-l-1 找下一个

'''


'''
解法一: 时间复杂度 O(n*k)
'''
def findmin(A, s, e):
    """
    @param A: A positive integer which has N digits, A is a string
    """
    r = float('inf')
    i = -1
    for j in range(s, e):
        if int(A[j]) < r:
            r = int(A[j])
            i = j
    return i
    

class Solution2:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write your code here
        n = len(A)
        l = n - k  # digits to keep
        s = 0
        res = ''
        while l > 0:
            i = findmin(A, s, n-l+1)
            res += A[i]
            s = i+1
            l -= 1
        return str(int(res))
        
'''
解法二：
因为我们要求最小的数，所以需要让排在最前的数字较小就可以，
要做到这一点，我们依次比较两个相邻的数字，如果前一个数字比后一个数字大，则将前一个数字删除；
如果前一个数字比后一个数字小，则不变，继续比较后面的数字。当进行到最后一个数字时，不需要再比较，直接将其删除即可。

在上面的例子 A="178542", k=4 中，
首先比较 1, 7; i++ 指向 7
然后比较 7, 8; i++，指向 8
比较    8, 5; 删掉 8，指向 7
比较    7, 5; 删掉 7，指向 1
比较    1, 5; i++  
        
时间复杂度 O(n)
'''

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write your code here
        if k == 0:
                    return A
        i = 0
        while i < len(A) - 1:
            if A[i] > A[i+1]:
                if i == 0:
                    A = A[1:]
                else:
                    A = A[:i] + A[i+1:]
                    i -= 1
                if k > 1:
                    k -= 1
                else:
                    return str(int(A))
            else:
                i += 1
        return str(int(A[:-k]))
            



if __name__ == '__main__':
    s = Solution()
    #print(s.DeleteDigits("123456789", 1))
    #print(s.DeleteDigits("90249", 2))
    #print(s.DeleteDigits("178542", 4))
    #print(s.DeleteDigits("90249", 2))
    print(s.DeleteDigits("10009876091", 4))
    