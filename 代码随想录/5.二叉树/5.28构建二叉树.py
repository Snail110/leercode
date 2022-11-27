class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


# 根据后序遍历和中序遍历的list，构建二叉树
"""
以 后序遍历的最后一个元素为切割点，先切中序遍历，根据中序遍历得到的左右两个子树后，再反过来，对后序遍历（除用过扽元素外）进行切割
依次类推 先右后左，直到没办法切割终止，然后移动切割点，继续切割
1、切割中序遍历list，按照后序遍历的最后元素切割即可
2、切割后序遍历list，需要按照切割后的左右中序遍历的长度来切割

递归函数
"""

class Solution:

    def splitList(self, res: list, value: int):
        """
        分割list
        :param res:
        :param value:
        :return:
        """
        for i in range(len(res)):
            if res[i] == value:
                return res[:i], res[i+1:]
    def buildTree(self,midOrder:list,postOrder:list):
        # 1、空，返回
        if len(midOrder) == 0:
            return
        # 2、选取后序遍历最后一个选取
        value = postOrder.pop()
        # 创建叶子节点
        root = TreeNode(value)
        if len(postOrder) == 1:
            return root

        # 切割中序遍历
        leftMidOrder,rightMidOrder = self.splitList(midOrder,value)
        # 切割后序遍历 按照左右切割中序的长度分别切割
        leftpostOrder = postOrder[:len(leftMidOrder)]
        rightpostOrder = postOrder[len(leftMidOrder):]

        # 左右递归
        root.left = self.buildTree(leftMidOrder,leftpostOrder)
        root.right = self.buildTree(rightMidOrder, rightpostOrder)

        return root

    def main(self,midOrder:list,postOrder:list):
        if len(midOrder) == 0 and len(postOrder) == 0:
            return
        return self.buildTree(midOrder,postOrder)



def preOrderTrversal(root:TreeNode,vec:list):
    """
    前序遍历 递归
    :param vec:
    :return: vec
    """
    # 终止条件
    if root == None:
        return
    vec.append(root.value)
    preOrderTrversal(root.left,vec)
    preOrderTrversal(root.right,vec)
    return vec

def midOrderTrversal(root:TreeNode,vec:list):
    """
    中序遍历 递归
    :param vec:
    :return: vec
    """
    # 终止条件
    if root == None:
        return
    midOrderTrversal(root.left,vec)
    vec.append(root.value)
    midOrderTrversal(root.right,vec)
    return vec

s = Solution()
midOrder = [9,3,15,20,7]
postOrder = [9,15,7,20,3]
root = s.main(midOrder,postOrder)
vec = []
print(midOrderTrversal(root,vec))