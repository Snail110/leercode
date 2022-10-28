"""
从nums中找到某一个元素数量大于一半
摩尔投票算法
"""
class Solution:
    def main(self,nums:list):

        count = 0   # 记录当前元素的个数
        res = -1    # 记录当前元素
        len_ = len(nums)
        for i in range(len_):
            if count == 0:
                res = nums[i]
            if nums[i] == res:
                count += 1
            else:
                count -= 1

        cnt = 0
        for i in range(len_):
            if nums[i] == res:
                cnt += 1
        return True if cnt * 2 > len_ else -1

nums = [1,2,5,5,5,5,9,9]
s = Solution()
print(s.main(nums))
