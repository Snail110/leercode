"""
cost = [10,15,20]
爬楼梯先付钱可以，爬上一层或者两层楼梯，给定cost，问下花费最小可以登顶
第一步：确定dp[i]的定义：爬到当前第i层，花费的最小钱。

第二步：确定递推函数：因为是爬上那个楼梯，当前的楼梯对应的花费是必须的，因此必须有cost[i],dp[i] = min(dp[i-1],dp[i-2]) + cost[i]

第三步：初始化：dp[0] = cost[0],dp[1] = cost[1]
比如第一层，登上第0层，需要支付 cost[0] =10,因此dp[0] = 10
第一层同样因为支付了钱可以爬2层，也可以爬2层，因此dp[1] = 15
第四步：确定遍历顺序：从递推公式来看需要先确定i-1，i-2才能确定i，因此从左向右遍历

第五步：举例推导dp数组

"""


class Solution:
    def min_cost(self,cost:list):
        """
        dp[i] 到达i层，最小需要花费多少
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        :param cost:
        :return:
        """
        high = len(cost) # 代表最终有多少楼梯
        # 初始化
        dp = [0] * high
        dp[0] = cost[0]
        dp[1] = cost[1]
        #
        for i in range(2,high):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        # 选取最后两层的最低花费从这两层中选取最小的就是花费最小的
        res = min(dp[-1],dp[-2])
        return res

s = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
print(s.min_cost(cost))

