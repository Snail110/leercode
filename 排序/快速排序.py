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

class Solution:
    def quickSort(self,nums:list):
        # 终止条件
        if len(nums) < 2:
            return nums

        mid = nums[len(nums)//2]

        left = []
        right = []
        nums.remove(mid)

        for i in nums:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        return self.quickSort(left) + [mid] + self.quickSort(right)

class Solution1:
    def partition(self,nums, low, high):
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

    def quick_sort(self,nums,low,high):
        if low < high:
            pivot = self.partition(nums,low,high)
            print(nums)
            # 去除pivot这个值
            self.quick_sort(nums, low, pivot - 1)
            self.quick_sort(nums, pivot + 1, high)
        return nums



s = Solution()
nums = [1,3,2,5,4]
print(s.quickSort(nums))

s1 = Solution1()
print(s1.quick_sort(nums,0,len(nums)-1))