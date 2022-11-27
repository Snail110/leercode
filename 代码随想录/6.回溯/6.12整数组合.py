"""
给定一数组nums和整数K，按照数组的元素组相加为K，返回所有的组合，元素可以有重复
K=10，nums=[1,2,3]
回溯方法
"""
class Solution:
    def inter_combine(self,nums:list,res:list,path:list,target:int):
        """

        :param nums:
        :param res:
        :param path:
        :return:
        """
        # 终止条件
        if target <= 0:
            if target == 0:
                res.append(path[:])
            return
        # 回溯逻辑
        for i in range(len(nums)):
            target -= nums[i]
            path.append(nums[i])
            self.inter_combine(nums,res,path,target)
            target += nums[i]
            path.pop()

        return res

    def inter_combine2(self,nums:list,res:list,path:list,target:int,start_index:int):
        """
        不重复的元素
        :param nums:
        :param res:
        :param path:
        :return:
        """
        # 终止条件
        if target <= 0:
            if target == 0:
                res.append(path[:])
            return
        # 回溯逻辑
        for i in range(start_index,len(nums)):
            target -= nums[i]
            path.append(nums[i])
            self.inter_combine2(nums,res,path,target, i+1)
            target += nums[i]
            path.pop()

        return res

    def inter_combine3(self,nums:list,res:list,path:list,target:int,start_index:int):
        """
        不重复的组合
        :param nums:
        :param res:
        :param path:
        :return:
        """
        # 终止条件
        if target < 0:
            return
        if target == 0:
            res.append(path[:])
            return
        # 回溯逻辑
        for i in range(start_index,len(nums)):
            target -= nums[i]
            path.append(nums[i])
            self.inter_combine3(nums,res,path,target, i)
            target += nums[i]
            path.pop()

        return res

    def main(self,nums:list,target:int):
        if len(nums) == 0:
            return None

        res = []
        path = []
        # self.inter_combine(nums,res,path,target)
        # self.inter_combine2(nums,res,path,target,0)
        self.inter_combine3(nums,res,path,target,0)
        return res
s = Solution()

nums = [1,2,3]
target = 5

print(s.main(nums,target))






