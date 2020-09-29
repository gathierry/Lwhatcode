import random

# ====== quick sort ======
def partition(nums, l, r):
    x = nums[r]
    j = l - 1
    for i in range(l, r):
        if nums[i] < x:
            j += 1  # j always at the last number < x
            nums[i], nums[j] = nums[j], nums[i]
    nums[j + 1], nums[r] = nums[r], nums[j + 1]
    return j + 1
            
def quick_sort(nums, l, r):
    if l < r:
        mid = partition(nums, l, r)
        quick_sort(nums, l, mid - 1)
        quick_sort(nums, mid + 1, r)
# ========================

# ====== merge sort ======
def merge(nums1, nums2):
    ret = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            ret.append(nums1[i])
            i += 1
        else:
            ret.append(nums2[j])
            j += 1
    if i == len(nums1):
        ret += nums2[j:]
    elif j == len(nums2):
        ret += nums1[i:]
    else:
        raise Error()
    return ret

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = int(len(nums) / 2)
    l = merge_sort(nums[:mid])
    r = merge_sort(nums[mid:])
    return merge(l, r)
# ========================
    

if __name__ == '__main__':
    random.seed(42)
    nums = [random.random() for _ in range(10)]
    nums.append(nums[3]*1)
    print(nums)
    # quick_sort(nums, 0, len(nums) - 1)
    nums = merge_sort(nums)
    print(nums)