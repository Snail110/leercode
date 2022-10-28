"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]

#思路
"""
class Solution:
    def genertionNums(n: int):
        nums = [[0] * n for i in range(n)]  # 二维列表 错误做法：[[0] * 3] * 3,属于浅拷贝
        startx, starty = 0, 0
        loop = n // 2  # 循环圈数数
        offerset = 1  # 边界循环过的外围
        count = 1  # 填充的数值
        mid = n // 2 # 中间数值
        while loop > 0:
            for i in range(starty, n - offerset):
                nums[startx][i] = count
                count += 1
            for j in range(startx, n - offerset):
                nums[j][n - offerset] = count
                count += 1
            for i in range(n - offerset, startx, -1):
                nums[n - offerset][i] = count
                count += 1
            for j in range(n - offerset, starty, -1):
                nums[j][startx] = count
                count += 1
            startx += 1
            starty += 1
            offerset = offerset + 2
            loop -= 1

        if n%2!=0:
            nums[mid][mid] = count
        return nums
s = Solution
print(s.genertionNums(3))