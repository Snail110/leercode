"""
擦汗如排序通过构建有序序列，，对于未排序的数据，再已排序序列中从后向前扫描，找到相应位置并插入
算法步骤：
1.将第一待排序序列第一个元素作为一个有序序列，把第二个元素到最后一个元素当成未排序序列
2.从头到尾一次扫描未排序系序列，将扫描到的每个元素插入到有序序列的适当位置，如果待插入元素和有序序列元素相等，就插在后面。
"""

class insert:
    def sort(self,nums:list):
        """
        插入排序
        :param nums:
        :return:
        """
        for i in range(len(nums)-1):
            tmp = nums[i+1]
            m = i
            # 在while循环判断条件时m,tmp 与当前的元素比较也是一种判断条件，只有小于了才进入循环，否则不会循环插入
            while m >= 0 and tmp < nums[m]:

                nums[m+1] = nums[m]
                m -= 1
            nums[m + 1] = tmp
        return nums


nums = [1,3,3,4,2,1]

s = insert()
print(s.sort(nums))

