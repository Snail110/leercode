"""
给出一个完全二叉树，求出该树的节点个数。

示例 1：

输入：root = [1,2,3,4,5,6]
输出：6
示例 2：

输入：root = []
输出：0
示例 3：

输入：root = [1]
输出：1
提示：

树中节点的数目范围是[0, 5 * 10^4]
0 <= Node.val <= 5 * 10^4
题目数据保证输入的树是 完全二叉树

完全二叉树:
完全二叉树只有两种情况，情况一：就是满二叉树，情况二：最后一层叶子节点没有满。

对于情况一，可以直接用 2^树深度 - 1 来计算，注意这里根节点深度为1。

对于情况二，分别递归左孩子，和右孩子，递归到某一深度一定会有左孩子或者右孩子为满二叉树，然后依然可以按照情况1来计算。
"""


class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 普通二叉树
# class Solution:
#     def TreeNodeNums(self,root:TreeNode):
#         """
#
#         :param root:
#         :return: nums
#         """
#         if root == None:
#             return 0
#         # 左
#         leftTreeNums = self.TreeNodeNums(root.left)
#         # 右
#         rightTreeNums = self.TreeNodeNums(root.right)
#         # 中
#         TreeNums = 1 + leftTreeNums + rightTreeNums
#         return TreeNums


# 完全二叉树
class Solution:
    def allTreeNums(self,root:TreeNode):
        # 终止条件
        if root == None:
            return 0
        # 分别求出left和right判断是否满二叉树
        leftNode = root.left
        rightNode = root.right
        leftNums = 0
        rightNums = 0

        while (leftNode):
            leftNode = leftNode.left
            leftNums += 1

        while (rightNode):
            rightNode = rightNode.left
            rightNums += 1

        if leftNums == rightNums:
            return (2 << leftNums) - 1
        return self.allTreeNums(root.left) + self.allTreeNums(root.right) + 1



root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(1);root.left.right = TreeNode(1)


s = Solution()
print(s.allTreeNums(root))



