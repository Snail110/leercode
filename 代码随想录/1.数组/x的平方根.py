"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：

输入：x = 4
输出：2

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def x_sqrt(self,x:int):
        """

        :param x:
        :return:
        """
        left = 0
        right = x + 1 # 0和1的存在
        ans = 0
        # 设置最大区间 left right
        while left < right:
            # 找到二分界限
            mid = (right - left) // 2 + left
            # 判断条件
            if mid * mid <= x:
                ans = mid
                # 更新左区间
                left = mid + 1
            else:
                # 更新右区间
                right = mid

        return ans

s = Solution()
x = 4
print(s.x_sqrt(x))
