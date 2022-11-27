class Solution:
    def bag01(self,value:list,weight:list,maxValue:int):
        """
        dp[j] = max(dp[j],dp[j-weight[i]]+value[i])
        先遍历物品，再便利背包重量
        :param value:
        :param weight:
        :return:
        """

        # 确定dp[j]含义：背包重量为j时，所装的最大价值
        # 递归公式 dp[j] = max(dp[j],dp[j-weight[i]]+value[i])
        # 初始化 最大重量 dp[0] = 0
        dp = [0] * (maxValue+1)

        # 先遍历物品，后遍历背包重量
        for i in range(len(weight)):
            for j in range(maxValue,weight[i]-1,-1):
                # 递归公式
                dp[j] = max(dp[j],dp[j-weight[i]] + value[i])

        return dp[maxValue]

s = Solution()
weight = [1, 3, 4]
value = [15, 20, 30]
bag_weight = 4

print(s.bag01(value,weight,bag_weight))
