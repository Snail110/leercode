"""
两个非递减数组nums1，nums2,排序在nums1中
"""

class Solution:
    def sort2nums(self,nums1:list,nums2:list,m:int,n:int):
        """
        :param nums1:
        :param nums2:
        :param m:
        :param n:
        :return:
        """
        nums1_len = len(nums1) - 1
        while n > 0 and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[nums1_len] = nums1[m-1]
                m -= 1
            else:
                nums1[nums1_len] = nums2[n - 1]
                n -= 1
            nums1_len -= 1
        # 把nums2的剩余的元素也放进来，nums1的剩余元素不需要放进来了，已经在里面
        for i in range(n):
            nums1[i] = nums2[i]
        return nums1

s = Solution()
nums1 = [7,9,10,0,0,0,0,0]
nums2 = [1,2,5,6,8]
print(s.sort2nums(nums1,nums2,3,5))
