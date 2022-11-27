"""
移除数组元素
给定一个数组nums和一个值valu，需要原地移除所有数值等于val的元素，并且返回移除后数组的新长度
"""
class Solution:
    def remove_value(self,nums:list,val:int):
        """

        :param nums:
        :param val:
        :return:
        """
        low = 0
        fast = 0
        len_ = len(nums)
        while fast < len_:
            if nums[fast] != val:
                nums[low] = nums[fast]
                low += 1
            fast += 1

        return nums[:low]

nums = [1,3,2,2,4]
val = 2
s = Solution()
print(s.remove_value(nums,val))


class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pre_order_tree(self,root:TreeNode,res:list):
        """
        前序遍历
        :param root:
        :param res:
        :return:
        """
        # 终止条件
        if root is None:
            return
        res.append(root.val)

        self.pre_order_tree(root.left,res)
        self.pre_order_tree(root.right,res)

        return res

    def mid_order_tree(self,root:TreeNode,res:list):
        """
        中序遍历
        :param root:
        :param res:
        :return:
        """
        # 终止条件
        if root is None:
            return
        self.mid_order_tree(root.left,res)
        res.append(root.val)
        self.mid_order_tree(root.right,res)

        return res

    def after_order_tree(self,root:TreeNode,res:list):
        """
        后序遍历
        :param root:
        :param res:
        :return:
        """
        # 终止条件
        if root is None:
            return
        self.after_order_tree(root.left,res)
        self.after_order_tree(root.right,res)
        res.append(root.val)

        return res


    def main(self,root:TreeNode):

        res = []
        res = self.after_order_tree(root,res)

        return res

s = Solution()

root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(3)

root.left.left = TreeNode(4);root.left.right = TreeNode(5)
root.right.left = TreeNode(6);root.right.right = TreeNode(7)


print(s.main(root))


"""
子集问题
"""
class Solution:
    def sub_nums(self,nums:list,path:list,res:list,start_index:int):
        """

        :param nums:
        :return:
        """
        # 终止条件
        res.append(path[:])
        if start_index >= len(nums):
            return

        for i in range(start_index,len(nums)):
            path.append(nums[i])
            self.sub_nums(nums,path,res,i+1) # 这里就要采用i了，而不是固定不变的 start_index
            path.pop()

        return res

    def main(self,nums:list):
        res = []
        path = []
        start_index = 0
        res = self.sub_nums(nums,path,res,start_index)
        return res

s = Solution()
nums = [1,2,3]
print(s.main(nums))


"""
跳跃问题 
贪心问题，不断地在最大范围内迭代，每次都判断 更新覆盖的最大范围，最大范围超过最长就代表跳到了最后
"""
class Solution:
    def skip_max_step(self,nums:list):
        """

        :param nums:
        :return:
        """

        max_step = 0
        #
        for i in range(len(nums),max_step):
            step = nums[i]
            max_step = max(max_step,i + step)

            if max_step >= len(nums) - 1:
                return True

        return False

nums = [3,2,1,0,4]
s = Solution()
print(s.skip_max_step(nums))


"""
最长递增子序列
"""


