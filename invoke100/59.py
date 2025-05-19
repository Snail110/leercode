class Solution:
    def generationMatrix(self,n):
        left,right,top,botton = 0,n-1,0,n-1
        order = [[-1] * n for i in range(n)]
        o = 1
        while o <= n * n:
            # left right,top booton 只是循环的边界
            for i in range(left,right+1):
                order[top][i] = o
                o +=1
            top += 1
            # top要+1
            for j in range(top,botton+1):
                order[j][right] = o
                o += 1
            right -= 1
            for m in range(right,left-1,-1):
                order[botton][m] = o
                o += 1
            botton -= 1
            for k in range(botton,top-1,-1):
                order[k][left] = o
                o += 1
            left +=1
        return order
    
s = Solution()
print(s.generationMatrix(3))

