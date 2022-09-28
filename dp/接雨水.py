class Solution:
    def trap(self,height:list):
        if len(height) == 0:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n-1)
        # 左边最大
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])

        rightMax = [0] * (n - 1) + [height[n-1]]
        # 左边最大
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        ans = 0
        for i in range(n):
            ans += min(leftMax[i],rightMax[i])-height[i]
        return ans

height = [0,1,0,2,0,0,1]

s = Solution()
print(s.trap(height))