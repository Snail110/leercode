"""
冒泡排序 bubble sort 重复地走访过要排序的数列，一次比较两哥元素，如果他们顺序错误，就把他们的交换过来，
走访数列的工作时重复地进行指导没有再需要交换，排序完成。

1.算法步骤：
1.比较相邻的元素，如果第一个比第二哥大，就交换他们两个，
2.对每一对相邻元素做同样的工作，从开始第一对到最后一对，这步做完后，最后的元素回事最大数。
3.针对素有的元素重复以上的步骤，除了最后一个。

"""

class Bubble:
    def sort(self,nums:list):
        """
        冒泡排序，
        :param nums:
        :return:
        """

        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        return nums


nums = [1,3,3,4,2]

f = Bubble()
print(f.sort(nums))