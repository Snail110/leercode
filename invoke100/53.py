class Solution:
    def maxSumArray(self,nums):
        # 动态规划方法 以下标i为单结尾的最大子和为maxsum[i],那么公式为
        # maxSUm[i] = max(maxsSUm[i-1] + nums[i],nums[i])
        # 错误的公式为：这个表示的是0-i内的所有最大子和
        # maxSum[i] = maxSum[i-1] + max(nums[i],0)
        maxSum = nums[0] # 当前最大子和数
        pre = 0 # 前一个最大子和数
        for i in nums:
            pre = max(pre + i, i)
            maxSum = max(maxSum, pre)
        return maxSum
    def maxSumArray1(self,nums):
        # 动态规划方法如果当前和maxSum>0,那么加上后会有增益，如果<0那么sum=当前值num[i]，
        ans = nums[0] # 当前最大子和数
        maxSum = 0
        for i in nums:
            if maxSum>0:
                maxSum = maxSum + i 
            else:
                maxSum = i
            ans = max(ans, maxSum)
        return ans
    def maxSumArray2(self,nums):
        # 标准DP
        # 动态规划方法 以下标i为单结尾的最大子和为maxsum[i],那么公式为
        # maxSUm[i] = max(maxsSUm[i-1] + nums[i],nums[i])
        # 错误的公式为：这个表示的是0-i内的所有最大子和
        # maxSum[i] = maxSum[i-1] + max(nums[i],0)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxSum= nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+ nums[i],nums[i])
            maxSum = max(maxSum, dp[i])
        return maxSum

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSumArray2(nums))
