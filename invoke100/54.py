class Solution:
    def spiralOrder(self,matrix):
        m = len(matrix[0]) # 列
        n = len(matrix) # 行
        if not matrix or not matrix[0]:
            return list
        rows,columns= len(matrix),len(matrix[0])
        order = list() # 存储逆时针遍历
        left,right,top,botton = 0,columns-1,0,rows-1 # 初始化四个边界，不断的缩圈
        while left <= right and top <= botton:
            #行从左到右
            for column in range(left,right+1):
                order.append(matrix[top][column])
            # 列，从上到下
            for row in range(top+1,botton+1):
                order.append(matrix[row][right])
            # 边界停止条件
            if left < right and top < botton:
                # 行，从右到左
                for column in range(right-1,left,-1):
                    order.append(matrix[botton][column])
                # 列，从下到上
                for row in range(botton-1,top,-1):
                    order.append(matrix[row][left])
            # 缩小范围
            left,right,top,botton = left+1,right-1,top+1,botton-1
        return order

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))