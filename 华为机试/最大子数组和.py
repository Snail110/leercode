"""
最大子数组和
给定一个整数数组nums，找出以最大和的连续子数组和（子数组最少包含一个元素），返回最大和

1、贪心算法：
设置一个res变量记录最大和，count记录当前和
i不断地从左到右遍历数组，当出现count<0时，那么将count重置为0，从i+1开始重新遍历，
如果count>0继续遍历，并且不断地更新res。
2、动态规划

"""

class Solution:
    def main(self,nums:list):

        res = 0
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            # 当出现小于0，说明当前的nums[i]不能用了，因此需要换下一个子数组重新开始
            if count < 0:
                count = 0
            else:
                res = max(res,count)

        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.main(nums))

