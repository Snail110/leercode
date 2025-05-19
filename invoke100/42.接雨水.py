class Solution:
    def trap(self, height):
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) -1
        ans = 0
        while left < right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(height))