"""
你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。
示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1
 

提示：

1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

动态规划
1,define
dp[i][j]表示长为i，宽为j的信封最大能套多少信封
2，递推公式
dp[i][j] = dp[i-m][j-n] + 1

3. 初始化
dp[0][j] = 0
dp[i][0] = 0

4.遍历：
for i in range(len(envelopes)):
    for m in range(envelopes[i][0]):
        for n in range(envelopes[i][1]):
            dp[i][j] = dp[i-m][j-n] + 1

"""

# class Solution:
#     def main(self,envelopes:list):
#         i_max = 0
#         j_max = 0
#         for i in range(len(envelopes)):
#             i_max = max(i_max,envelopes[i][0]+1)
#             j_max = max(j_max,envelopes[i][1]+1)
#
#         dp = [[1 for _ in range(j_max)] for _ in range(i_max)]
#
#         for k in range(len(envelopes)):
#             i = envelopes[k][0]
#             j = envelopes[k][1]
#             for l in range(len(envelopes)):
#                 m = envelopes[l][0]
#                 n = envelopes[l][1]
#                 if m < i and n < j:
#                     dp[i][j] = max(dp[i][j],dp[m][n] + 1)
#         res = 0
#         for k in range(len(envelopes)):
#             i = envelopes[k][0]
#             j = envelopes[k][1]
#             res = max(res,dp[i][j])
#         return res

# 先对nums按照key1，key2排序，然后看key2的严格最长递增序列长度就行了。


envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]] # [[2,3],[5,4],[6,7],[6,8]]
envelopes = sorted(envelopes,key = lambda x:(x[0],-x[1]))
s = Solution()
print(s.main(envelopes))

