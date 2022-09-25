"""
由长度为length的array表示的整数，允许相邻位数交换，求n步交换内能得到的最大整数
排序 将最大值都放在最高位，0不能放在第一位

解法：贪心算法，n步交换可以将最远的n距离的位数交换过来，那么利用贪心算法：首先将n步内的最大值与当前的i位置进行交换，
然后计算剩余多少步数，进一步在剩余步数区间内的最低值再次交换。
"""

class Solution:
    def getMaxNumStep(self,nums:list):
        max_val = -1
        step = -1
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                step = i
        return max_val,step

    def MaxNum(self,nums:list,n:int):
        nums_len = len(nums)
        i = 0
        while n > 0 and i < nums_len:
            max_val,step = self.getMaxNumStep(nums[i:i+n+1])
            tmp = nums[i]
            nums[i] = max_val
            nums[i+step] = tmp
            n = n - step
            i += 1
        return nums

s = Solution()
nums = [1,3,2,1]
print(s.MaxNum(nums,0))