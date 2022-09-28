"""
有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。

# 二维dp数组01背包

依然动规五部曲分析一波。

1.确定dp数组以及下标的含义
对于背包问题，有一种写法， 是使用二维数组，即dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。

只看这个二维数组的定义，大家一定会有点懵，看下面这个图：

2.确定递推公式
再回顾一下dp[i][j]的含义：从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。

那么可以有两个方向推出来dp[i][j]，

1).不放物品i：由dp[i - 1][j]推出，即背包容量为j，里面不放物品i的最大价值，此时dp[i][j]就是dp[i - 1][j]。(其实就是当物品i的重量大于背包j的重量时，物品i无法放进背包中，所以被背包内的价值依然和前面相同。)
2).放物品i：由dp[i - 1][j - weight[i]]推出，dp[i - 1][j - weight[i]] 为背包容量为j - weight[i]的时候不放物品i的最大价值，那么dp[i - 1][j - weight[i]] + value[i] （物品i的价值），就是背包放物品i得到的最大价值
所以递归公式： dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);


3.dp数组如何初始化
关于初始化，一定要和dp数组的定义吻合，否则到递推公式的时候就会越来越乱。

首先从dp[i][j]的定义出发，如果背包容量j为0的话，即dp[i][0]，无论是选取哪些物品，背包价值总和一定为0。如图：

状态转移方程 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]); 可以看出i 是由 i-1 推导出来，那么i为0的时候就一定要初始化。

dp[0][j]，即：i为0，存放编号0的物品的时候，各个容量的背包所能存放的最大价值。

那么很明显当 j < weight[0]的时候，dp[0][j] 应该是 0，因为背包容量比编号0的物品重量还小。

当j >= weight[0]时，dp[0][j] 应该是value[0]，因为背包容量放足够放编号0物品。

for (int j = 0 ; j < weight[0]; j++) {  // 当然这一步，如果把dp数组预先初始化为0了，这一步就可以省略，但很多同学应该没有想清楚这一点。
    dp[0][j] = 0;
}
// 正序遍历
for (int j = weight[0]; j <= bagweight; j++) {
    dp[0][j] = value[0];
}

dp[0][j] 和 dp[i][0] 都已经初始化了，那么其他下标应该初始化多少呢？

其实从递归公式： dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]); 可以看出dp[i][j] 是由左上方数值推导出来了，那么 其他下标初始为什么数值都可以，因为都会被覆盖。

4.确定遍历顺序

先遍历 物品还是先遍历背包重量呢？

其实都可以！！ 但是先遍历物品更好理解。

那么我先给出先遍历物品，然后遍历背包重量的代码。
// weight数组的大小 就是物品个数
for(int i = 1; i < weight.size(); i++) { // 遍历物品
    for(int j = 0; j <= bagweight; j++) { // 遍历背包容量
        if (j < weight[i]) dp[i][j] = dp[i - 1][j];
        else dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);

    }
}


"""
# 二维数组dp
# class Solution:
#     def maxValue01Bag(self,value:list,weight:list,bag_size:int):
#         # dp含义
#         rows, cols = len(weight), bag_size + 1
#         dp = [[0 for _ in range(cols)] for _ in range(rows)]
#         # 初始化dp
#         # 选取i-1个物品，背包最大总量为0，价值也为0
#         for i in range(rows):
#             dp[i][0] = 0
#
#         # 选取第一个物品 如果其重量小于最大重量，最大价值为第一个物品价值
#         first_item_weight, first_item_value = weight[0], value[0]
#         for j in range(1,cols):
#             if first_item_weight <= j:
#                 dp[0][j] = first_item_value
#         #遍历顺序 先物品后重量
#         for i in range(1,rows):
#             for j in range(1,cols):
#                 if weight[i] > j:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]] + value[i])
#
#         return dp


# 一维数组dp
"""
一维dp数组（滚动数组）
动规五部曲分析如下：

确定dp数组的定义
在一维dp数组中，dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]。

一维dp数组的递推公式
dp[j]为 容量为j的背包所背的最大价值，那么如何推导dp[j]呢？

dp[j]可以通过dp[j - weight[i]]推导出来，dp[j - weight[i]]表示容量为j - weight[i]的背包所背的最大价值。

dp[j - weight[i]] + value[i] 表示 容量为 j - 物品i重量 的背包 加上 物品i的价值。（也就是容量为j的背包，放入物品i了之后的价值即：dp[j]）

此时dp[j]有两个选择，一个是取自己dp[j] 相当于 二维dp数组中的dp[i-1][j]，即不放物品i，一个是取dp[j - weight[i]] + value[i]，即放物品i，指定是取最大的，毕竟是求最大价值，

dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

一维dp数组如何初始化

dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]，那么dp[0]就应该是0，因为背包容量为0所背的物品的最大价值就是0。
一维dp数组遍历顺序

for(int i = 0; i < weight.size(); i++) { // 遍历物品
    for(int j = bagWeight; j >= weight[i]; j--) { // 遍历背包容量
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

    }
}

倒序遍历是为了保证物品i只被放入一次！。但如果一旦正序遍历了，那么物品0就会被重复加入多次！

举一个例子：物品0的重量weight[0] = 1，价值value[0] = 15

如果正序遍历

dp[1] = dp[1 - weight[0]] + value[0] = 15

dp[2] = dp[2 - weight[0]] + value[0] = 30

此时dp[2]就已经是30了，意味着物品0，被放入了两次，所以不能正序遍历。

为什么倒序遍历，就可以保证物品只放入一次呢？

倒序就是先算dp[2]

dp[2] = dp[2 - weight[0]] + value[0] = 15 （dp数组已经都初始化为0）

dp[1] = dp[1 - weight[0]] + value[0] = 15

"""

class Solution:
    def maxValue01Bag(self,value:list,weight:list,bag_size:int):
        """
        一维dp
        :param value:
        :param weight:
        :param bag_size:
        :return:
        """
        rows,cols = len(weight),bag_size + 1
        # 初始化
        dp = [0 for _ in range(cols)]

        for i in range(0,rows):
            for j in range(cols-1,weight[0]-1,-1):
                if weight[i] > j:
                    dp[j] = dp[j]
                else:
                    dp[j] = max(dp[j],dp[j-weight[i]] + value[i])

        return dp

bag_size = 5
weight = [1, 3, 4]
value = [15, 20, 30]

s = Solution()

print(s.maxValue01Bag(value,weight,bag_size))




