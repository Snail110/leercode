"""
有一堆书， 要是书的长宽都大于（不是>=，是>）另外一本书，则可以叠放上面，求最大叠的层数
例子：
输入：[[20,16],[15,11],[10,10],[9,10]] （里面的每一个数组都代表一本书）
输出 3

解答：
现将信封按照x0递增排序，x1按照递减排序，变成求 一维的最长递增子序列

"""

class Solution:
    def max_layers(self,nums:list):
        """

        :param nums:
        :return:
        """
        nums_s = sorted(nums,key=lambda x:(x[0],-x[1]))
        nums_2 = [i[1] for i in nums_s]

        len_ = len(nums_2)
        # dp问题 定义：dp[i]:以i结尾的最长上升子序列长度
        dp = [1] * (len_+1)

        for i in range(len_):
            for j in range(i):
                if nums_2[j] < nums_2[i]:
                    dp[i] = max(dp[i],dp[j] + 1)

        return max(dp)

nums = [[20,16],[15,11],[9,9],[9,10]]

s = Solution()
print(s.max_layers(nums))




