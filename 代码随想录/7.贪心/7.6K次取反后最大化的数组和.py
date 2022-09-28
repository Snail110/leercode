"""
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

示例 1：

输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：

输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
示例 3：

输入：A = [2,-3,-1,5,-4], K = 2
输出：13
解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。

贪心的思路，局部最优：让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。

第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
第二步：从前向后遍历，遇到负数将其变为正数，同时K--
第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
第四步：求和

"""

class Solution:

    def maxsumNums(self,nums:list,K:int):
        # 按照 abs进行排序
        nums_s = sorted(nums,key = lambda x:abs(x),reverse = True)
        for i in range(len(nums_s)):
            if nums_s[i] < 0:
                nums_s[i] *= -1
                K -= 1
        # 剩余的k选取最小abs值的进行反转
        if K%2 == 1:
            nums_s[-1] *= -1
        result = sum(nums_s)
        return result

s = Solution()
# A = [3,-1,0,2]; K = 3

A = [2,-3,-1,5,-4]; K = 2
print(s.maxsumNums(A,K))


