"""
接雨水，N个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨后能接多少雨水

"""
class Solution:
    def water_area(self,hright:list):
        """
        计算每个柱子的左右高度，然后选取最低的一边决定最多能接多少雨水，再减去height
        :return:
        """
        n = len(height)
        # 统计左边高度
        left_high_max = [height[0]] + [0] * (n-1)
        # 统计右边高度
        right_high_max = [0] * (n-1) + [height[-1]]

        for i in range(1,n):
            left_high_max[i] = max(left_high_max[i-1],height[i])

        print(left_high_max)
        for i in range(n-2,-1,-1):
            right_high_max[i] = max(right_high_max[i + 1], height[i])
        print(right_high_max)
        res = 0
        for i in range(n):
            res += min(right_high_max[i],left_high_max[i]) - height[i]
        return res
height = [0,1,0,2,0,0,1]

s = Solution()
print(s.water_area(height))