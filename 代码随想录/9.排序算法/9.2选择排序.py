"""
选择排序 无论什么数据进去都i是o（n**2）的时间复杂度，用到时数据规模越小越好，不占用额外内存空间
1.算法步骤：
1.搜先在未排序序列中找到最小（大）元素，再存放到排序序列的起始位置
2.再从v剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾，
3.重复第二步，直到所有元素均排序完毕。

"""

class Select:
    def sort(self,nums:list):
        """
        选择排序
        :param nums:
        :return:
        """

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                print(j)
                if nums[j] < nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]

        return nums
nums = [1,3,3,4,2]

f = Select()
print(f.sort(nums))