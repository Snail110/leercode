"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]

#思路
因为题目说了需要不重复的集合，因此需要排序
排序 + 双指针
固定一个数，然后用双指针循环剩下的数据

"""
class Solution:
    def three_number_sum(self,nums:list):

        s_nums = sorted(nums)
        n = len(s_nums)
        res = []
        for i in range(n):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            a = 0 - s_nums[i]

            left = i + 1
            right = n - 1
            while left < right:
                if s_nums[left] + s_nums[right] < a:
                    left += 1
                elif s_nums[left] + s_nums[right] > a:
                    right -= 1
                else:
                    res.append([s_nums[i],s_nums[left],s_nums[right]])
                    left += 1

        return res



nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.three_number_sum(nums))


