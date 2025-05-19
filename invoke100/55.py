class Solution:
    def jump2(self,nums):
        maxPos = nums[0]
        ll = len(nums)
        for i in range(ll):
            # 判断是否可以达到当前位置，如果达不到直接返回false，如果达到更新最大距离
            if maxPos >= i:
                # 更新最大距离
                maxPos=max(maxPos,nums[i] + i)
                # 判断是否达到了终点，到达了立即返回True
                if maxPos >= ll-1:
                    return True
        return False
        
s = Solution()
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(s.jump2(nums))