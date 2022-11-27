
"""
# n行的二维数组，输出第一列是真实标签，第二列是分数，（0-1）
# 输出n行逆序对数量

0.8,0.6
0.7,0.5
0.9,0.4

n 一维数组 0.8,0.9,0.7

求：多少个逆序对

class Solution:
    def __init__(self):
        self.res = 0
    def trac(self,nums:list,path:list,start_index:int):
        # 终止条件
        if len(path) == 2:
            if path[0] < path[1]:
                self.res += 1
            return

        for i in range(start_index,len(nums)):
            path.append(nums[i])
            self.trac(nums,path,i)
            path.pop()

        return self.res

    def main(self,nums:list):
        path = []
        start_index = 0

        self.trac(nums,path,start_index)
        return self.res

s = Solution()

nums = [0.8,0.9,0.7]
print(s.main(nums))
"""

nums = [8,0,3,2,5,0,4,2]
def partition(nums, low, high):
    pivot = nums[high] # 以最右边的设置基准 那么计算low,high-1 之间的数据
    index = low - 1

    for j in range(low,high):
        if nums[j] < pivot:
            index += 1 # 索引右移
            nums[index],nums[j] = nums[j],nums[index] # 交换将小于基准的元素转移到左边
    # 这个时候小于pivot的元素在左边，大于pivot的数据在右边，然后将piovt也要加进去，那么与index+1（即肯定大于pivot）交换一下
    index += 1
    nums[index], nums[high] = nums[high], nums[index]  # 交换将小于基准的元素转移到左边
    # 返回index
    return index

def quick_sort(nums,low,high):
    if low < high:
        pivot = partition(nums,low,high)
        print(nums)
        # 去除pivot这个值
        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)
    return nums
print(quick_sort(nums,0,len(nums)-1))

def quick_sort_max_k(nums, k):
    mid = len(nums)//2
    if mid == k - 1:
        return nums[mid]
    left = []
    right = []

    nums.remove(nums[mid])

    for i in range(len(nums)):
        if nums[i] > nums[mid]:
            left.append(nums[i])
        else:
             right.append(nums[i])
    if mid > k-1:
        return quick_sort_max_k(left,k)
    else:
        return quick_sort_max_k(right,k-mid)

