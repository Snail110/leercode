"""
给定一数组nums和整数K，按照数组的元素组相加为K，返回所有的组合，元素可以有重复
K=10，nums=[1,2,3]
回溯方法
"""
class Solution:
    def numsK(self,nums:list,target:int,result:list,path:list):
        # 终止条件
        if target <= 0:
            if target == 0:
                result.append(path[:])
            return

        # 单层回溯逻辑
        for i in range(len(nums)):
            target -= nums[i]
            path.append(nums[i])
            self.numsK(nums,target,result,path)
            target += nums[i]
            path.pop()

        return result

    def main(self,nums:list,target:int):
        # 排序
        nums_sort = sorted(nums)
        path = []
        result = []
        self.numsK(nums_sort,target,result,path)
        return result


s = Solution()

nums = [1,2,3]
target = 5

print(s.main(nums,target))






