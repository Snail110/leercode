"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3 输出：4

解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2： 输入：strs = ["10", "0", "1"], m = 1, n = 1 输出：2 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100

转化为01背包，求最大值肯定有max()
1、定义dp[i][j]：包含i个0和j个1，最大子集为dp[i][j],物品是strs，背包是0和1的数量
2、递推公式: dp[i][j] = max(dp[i][j],dp[i-str[s][0]][j-str[s][1]] + 1)
3、初始化：dp[0][0] = 0,dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
4、遍历顺序：
for s in strs:
s_0 = count('0')
s_1 = count('1')
for i in range(m,s_0-1,-1):
for j in range(n,s_1-1,-1):
dp[i][j] = max(dp[i][j],dp[i-s_0][j-s_1] + 1)

"""
class Solution:
    def zero_and_one(self,strs:list,m:int,n:int):
        """

        :param strs:
        :param m:
        :param n:
        :return:
        """
        # init
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]


        for s in range(len(strs)):
            zero = strs[s].count('0')
            one = strs[s].count('1')
            for i in range(m,zero-1,-1):
                for j in range(n,one-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zero][j-one] + 1)

        return dp[m][n]

# strs = ["10", "0", "1"]
# m = 1
# n = 1
strs = ["10", "0001", "111001", "1", "0"]
m = 3
n = 3
print(Solution().zero_and_one(strs,m,n))
