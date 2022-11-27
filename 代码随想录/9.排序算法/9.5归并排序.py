"""
归并排序（merge sort）是建立在归并操作上的一种有效排序算法，该算法采用分治法的应用，有两种方法实现：
-自上而下的递归（所有的递归方法都可以用迭代重新写）
-自下而上的迭代
算法步骤：
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
2.设定两个指针，最初位置分别为两个已经排序序列的起始位置；
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一个位置
4.重复步骤3直到某一指针达到序列尾；
5.将另一个序列剩下的所有元素直接复制到合并序列尾
"""
from collections import deque

class Solution:
    def mergeSort(self, nums: list):
        """
        归并排序采用的后序遍历，先左 右，再中
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2    # 将nums一分为二
        left = nums[:mid]   # 左
        right = nums[mid:]  # 右
        return self.sort(self.mergeSort(left), self.mergeSort(right))

    def sort(self, left, right):
        res = []
        # 比较两者的最大值，然后放入res中
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        # 将最后没有排序的一次放进res中
        while len(left) > 0:
            res.append(left.pop(0))

        while len(right) > 0:
            res.append(right.pop(0))
        return res

nums = [1,3,4,2,10,9,5]

s = Solution()
print(s.mergeSort(nums))