class Solution:
    def main(self,num1,num2):
        n = len(num1)
        m = len(num2)
        right = m-1
        left = n-m-1
        while right >=0 and left >=0:
            if num2[right] > num1[left]:
                num1[n-1] = num2[right]
                right -=1
                n -=1
            else:
                num1[n-1] = num1[left]
                left -=1
                n -=1
        
        if right>=0:
            num1[0:right+1] = num2[0:right+1]
        return num1

s = Solution()
num1 = [1,2,5,6,0,0,0]
num2 = [3,4,7]

num1 = [5,6,8,0]
num2 = [1]

print(s.main(num1,num2))
            

