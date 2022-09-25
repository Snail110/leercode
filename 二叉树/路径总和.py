class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
# 112 路径总和
class Solution:
    def inSumPath(self,root:TreeNode,count:int):

        # 终止条件
        if count == 0 and root.left == None and root.right == None:
            return True

        # 单层回溯逻辑
        if root.left:
            count -= root.left.value
            # 及时返回值
            if self.inSumPath(root.left,count):
                return True
            count += root.left.value

        if root.right:
            count -= root.right.value
            # 及时返回值
            if self.inSumPath(root.right,count):
                return True
            count += root.right.value
        return False

    def main(self,root:TreeNode,count:int):
        if root == None:
            return False

        return self.inSumPath(root,count - root.value)

# 113路径总和2
# class Solution:
#     def inSumPath(self,root:TreeNode,count:int,result:list,path:list):
#
#         # 终止条件
#         if count == 0 and root.left == None and root.right == None:
#             result.append(path[:])
#
#         # 单层回溯逻辑
#         if root.left:
#             count -= root.left.value
#             path.append(root.left.value)
#             self.inSumPath(root.left,count,result,path)
#             count += root.left.value
#             path.pop()
#
#         if root.right:
#             count -= root.right.value
#             path.append(root.right.value)
#             self.inSumPath(root.right,count,result,path)
#             path.pop()
#         return result
#
#     def main(self,root:TreeNode,count:int):
#         if root == None:
#             return []
#         result = []
#         path = []
#         path.append(root.value)
#         count = count - root.value
#         result = self.inSumPath(root,count,result,path)
#         return result
root = TreeNode(1);root.right = TreeNode(2);root.left = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
count = 9
print(s.main(root,count))