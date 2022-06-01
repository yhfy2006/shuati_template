# 二分法

# 二分查找
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:  # 注意
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1

# 二分寻找左边界
def binary_search_left_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

# target 比所有数都大
# if (left == nums.length) return -1;
# 类似之前算法的处理方式
# return nums[left] == target ? left : -1;

# 二分寻找右边界
def binary_search_left_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1


# 滑动窗口
from collections import defaultdict
def sliding_window(s, t):
    need_dict = defaultdict(int)
    for c in t:
        need_dict[c] += 1

    left, right = 0, 0
    valid = 0

    while right < len(s):
        c = s[right] #要移入的char
        right += 1 #增大窗口

        # ... 进行窗口内的一系列更新

        # debug
        print(left, right)

        while valid == len(need_dict): # 窗口需要收紧
            d = s[left]
            left += 1

            # check if
            valid -= 1

# 回朔
res = []
track = []
def backtrack(nums, s):
    res.add([track])
    for i in range(len(nums)):
        track.append(nums[i])
        backtrack(nums, i + 1)
        track.pop()

def subsets(nums):
    backtrack(nums, 0)
    return res

# DFS

# BFS

# 拓扑