class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def sumPath(self,root:TreeNode,path:list,res_path:list):
        """
        前序遍历
        :param root:
        :param path:
        :param res_path:
        :return:
        """
        # 中
        path.append(root.value)
        # 终止条件
        if root.right == None or root.right == None:
            return res_path.append(path[:])

        # 回溯左
        if root.left:
            self.sumPath(root.left,path,res_path)
            path.pop()

        # 回溯右
        if root.right:
            self.sumPath(root.right,path,res_path)
            path.pop()

        return res_path

    # def sumPath(self,root:TreeNode,path:list,res_path:list):
    #     """
    #     前序遍历
    #     :param root:
    #     :param path:
    #     :param res_path:
    #     :return:
    #     """
    #     # 终止条件
    #     if root.right == None or root.right == None:
    #         return res_path.append(path[:])
    #
    #     # 回溯左
    #     if root.left:
    #         path.append(root.left.value)
    #         self.sumPath(root.left,path,res_path)
    #         path.pop()
    #
    #     # 回溯右
    #     if root.right:
    #         path.append(root.right.value)
    #         self.sumPath(root.right,path,res_path)
    #         path.pop()
    #
    #     return res_path

    def main(self,root:TreeNode):

        if root == None:
            return []
        res_path = []
        path = []
        self.sumPath(root,path,res_path)
        return res_path

root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.main(root))