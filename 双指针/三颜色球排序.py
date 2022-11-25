"""
具有3种颜色的球 红，黄，白，按照红、黄、白的顺序排序。
要求不能用自带的sort函数，并且为了方便起见，红=0，黄=1，白为2。
思路：
该题目是一个简单的排序，按照颜色排序，不要求数值精准排序，那么可以采用双指针的形式
left，index，right
left=0，right=n-1，index=0开始
依次向右移动index，与left比较，如果index为0，那么left和index交换，并同时向右移动
如果为index为1，1本身就不应该在左边，因此不交换，index+1，left不变，
如果index=2，那么跟right交换，并且right-1，index不变，因为不确定交换后index为多少，需要进一步判断对比。

"""

class Solution:
    def sort_ball(self, nums: list):
        """

        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1
        index = 0
        # 终止条件为index遍历到了right
        while index < right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1

        return nums

s = Solution()
nums = [0,1,2,0,1,2,1]
s.sort_ball(nums)
print(nums)