"""
快速排序使用分执治法策略把一个串行list分为两个子串行，在冒泡排序的基础上的递归分治法，
算法步骤：
1从数列中挑出一个元素，称为基准pivot
2重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准大的摆在基准的后面，在这个分组退出后，该基准就处于数列中间的位置，成为分区操作
3递归地把小小于基准元素的子数列和大于基准元素的子数列排序
4递归最底部就是数列的大小是0或者1，就是被永远排序好了，算法退出。

挖坑填数 + 分治法

对挖坑填数进行总结:

1．i =L; j = R; 将基准数挖出形成第一个坑a[i]。
2．j--由后向前找比它小的数，找到后挖出此数填前一个坑a[i]中。
3．i++由前向后找比它大的数，找到后也挖出此数填到前一个坑a[j]中。
4．再重复执行2，3二步，直到i==j，将基准数填入a[i]中。

"""
class Solution1:
    def partiton(self, nums, low, high):
        pivot = nums[high]

        index = low - 1
        for i in range(low,high):
            if nums[i] < pivot:
                index += 1
                nums[index],nums[i] = nums[i],nums[index]

        index += 1
        nums[index], nums[high] = nums[high], nums[index]
        return index

    def quick_sort(self,nums,low,high):
        """
        递归+分而治之思想，
        :param nums:
        :param low:
        :param high:
        :return:
        """
        # 终止条件 low < high
        if low < high:
            # 计算出分而治之的界限 pi
            pi = self.partiton(nums,low,high)
            # 去除pi界限
            self.quick_sort(nums,low,pi-1)
            self.quick_sort(nums,pi+1,high)

# s = Solution()
nums = [1,3,2,5,4,6,3]
# print(s.quickSort(nums))

s1 = Solution1()
s1.quick_sort(nums,0,len(nums)-1)
print(nums)