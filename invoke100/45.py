class Solution:
    def jump(self, nums):
        max_pos = 0
        begin = 0
        end = 0
        step = 0
        while end < len(nums) - 1:
            for i in range(begin,end+1):
                max_pos = max(max_pos,nums[i]+ i)
            begin = end
            end = max_pos
            step += 1
        return step
    

s = Solution()
nums = [2,3,1,1,4]
print(s.jump(nums))

