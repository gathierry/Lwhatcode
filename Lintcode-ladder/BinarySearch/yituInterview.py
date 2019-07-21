"""
依图科技面试题
数组 A: a[0], a[1], a[2] ..., a[n]
找出最短的 l，使得 a[i:i+l] 包含 A 中所有的元素

使用二分法搜索 l
给定 l 判断是否符合条件 O(n)
二分搜索 O(logn)
时间复杂度 O(nlogn)

"""

def checkl(A, l):
    if l == 0:
        return False
    num = len(set(A))
    d = {}
    for a in A[:l]:
        if a not in d:
            d[a] = 0
        d[a] += 1
    for i in range(len(A)-l):
        if len(d) == num:
            return True
        d[A[i]] -= 1
        if d[A[i]] == 0:
            del d[A[i]]
        if A[i+l] not in d:
            d[A[i+l]] = 0
        d[A[i+l]] += 1
    return False
        

def f(A):
    lb = 0
    ub = len(A)
    while lb < ub:
        l = (lb+ub) // 2
        if checkl(A, l):
            ub = l
        else:
            lb = l+1
    return lb
    
if __name__ == '__main__':
    A = [2,3,4,2,2,3]
    A = [1]
    A = [1,2]
    A = [1,1]
    A = []
    print(f(A))
    
    
    
            
        