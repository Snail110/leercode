
"""
三数之和， 相加=0
返回不重复的答案
"""
class Solution:
    def TreeSum(self,nums:list):
        """
        双指针 + set保存 + 排序nums + 返回值 该版本是去重复的三数之和
        :param nums:
        :return:
        """
        nums_sort = sorted(nums)
        size = len(nums_sort)
        # 判断最小值是否大0
        if nums_sort[0]>0:
            return []
        # 返回值
        res = []
        # 遍历i, 然后变为两数之和， mn指针不断逼近
        for i in range(size):
            # 该判断是去除重复的数组
            if i > 0 and nums_sort[i-1] == nums_sort[i]:
                continue
            tmp = 0 - nums_sort[i]
            m = i+1
            n = size - 1
            while m < n:
                if (nums_sort[m] + nums_sort[n]) > tmp:
                    n -= 1  # 从尾部逼近
                elif (nums_sort[m] + nums_sort[n]) < tmp:
                    m += 1  # 从头部逼近
                else:
                    res.append([nums_sort[i],nums_sort[m],nums_sort[n]])
                    n -= 1  # 从尾部逼近
                    m += 1  # 从头部逼近

        return res

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.TreeSum(nums))