"""
lc 17:
给定2-9的字符串，返回它能代表的字母组合

1、确定遍历对应，和遍历索引：对象是字符串（移动的遍历对象）遍历索引为index，变化的数组
"""
class Solution:
    def phone_word(self,nums:str):
        """

        :param nums:
        :return:
        """
        if len(nums) == 0:
            return []

        word_doct = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        path = []    # 保存回溯的中间结果
        res = []   # 保存最终结果

        def helper(index:int):
            """
            index 代表需要遍历的数字
            :param index:
            :return:
            """
            # 终止条件
            if len(path) == len(nums):
                res.append(path[:])
                return
            # 选取数字对应的字母
            word = word_doct[nums[index]]
            # 遍历字母串
            for i in word:
                path.append(i)
                helper(index + 1)
                path.pop()

        helper(0)
        return res

s = Solution()
nums = '23'
print(s.phone_word(nums))
