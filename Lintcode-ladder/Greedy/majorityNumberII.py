'''
参考 https://www.cnblogs.com/yuzhangcmu/p/4175779.html
与 Majority Number I 相似。但我们要保存 2 个 number.
1. 遇到第一个不同的值，先记录 number 2.
2. 新值与n1, n2都不同，则cnt1, cnt2都减少
3. 当n1, n2任意一个为 0 时，从新值中挑出一个记录下来。
4. 最后再对2个候选值进行查验，得出最终的解。

证明：

1. 我们对cnt1,cnt2减数时，相当于丢弃了3个数字（当前数字，n1, n2）。
也就是说，每一次丢弃数字，我们是丢弃3个不同的数字。而 Majority number 超过了 1/3 所以它最后一定会留下来。

设定总数为N, majority number 次数为 m。丢弃的次数是 x。则 majority 被扔的次数是 x
而 m > N/3, N - 3x > 0. 
3m > N,  N > 3x 所以 3m > 3x, m > x 也就是说 m一定没有被扔完
最坏的情况，Majority number每次都被扔掉了，但它一定会在n1,n2中。
'''

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        cnt1 = 0
        cnt2 = 0
        n1 = None
        n2 = None
        for n in nums:
            print(n, n1, n2, cnt1, cnt2)
            if n1 is None:
                n1 = n
                cnt1 = 1
                continue
            if n == n1:
                cnt1 += 1
                continue
            if n2 is None:
                n2 = n
                cnt2 = 1
                continue
            if n == n2:
                cnt2 += 1
                continue
            cnt1 -= 1
            cnt2 -= 1
            if cnt1 == 0:
                n1 = None
            if cnt2 == 0:
                n2 = None
            
        if n1 is None:
            return n2
        if n2 is None:
            return n1
        print(n1, n2)
        cnt1 = 0
        cnt2 = 0
        for n in nums:
            if n == n1:
                cnt1 += 1
                if cnt1 >= len(nums) // 3:
                    return n1
            elif n == n2:
                cnt2 += 1
                if cnt2 >= len(nums) // 3:
                    return n2
        
if __name__ == '__main__':
    s = Solution()
    #print(s.majorityNumber([1, 2, 1, 2, 1, 3, 3, 3, 1, 2]))
    #print(s.majorityNumber([7, 1, 7, 7, 61, 61, 61, 10, 10, 10, 61]))
    #print(s.majorityNumber([1, 1, 2]))
    print(s.majorityNumber([1, 2, 3, 4, 4, 5]))
