"""
二叉搜索树的删除操作：分为5种情况：
第一种：没有找到满足的节点，返回root
第二种：满足的节点，没有左右子节点，直接删除即可
第三种：满足的节点有左节点，没有右节点，直接删除后，将左节点接到头节点
第四种：满足的节点有右节点，没有左节点，直接删除后，将右节点接到头节点
第五种：满足的节点同时有左右节点，直接删除后，将左节点接到头节点，右节点接到右子树的最左叶子节点
"""
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def del_node(self,cur:TreeNode,value:int):
        """

        :param cur:
        :param value:
        :return:
        """
        if cur is None:
            return cur

        if cur.value == value:
            if cur.left is None and cur.right is None:
                return None
            elif cur.left and cur.right is None:
                return cur.left
            elif cur.left is None and cur.right:
                return cur.right
            else:
                right_cur = cur.right   # 被删除节点的右子树
                while right_cur.left is not None:
                    right_cur = right_cur.left
                right_cur.left = cur.left
                cur = cur.right     # 只要返回新的right，就相当于跳过了cur
                return cur

        if cur.value > value:
            cur.left = self.del_node(cur.left,value)
        if cur.value < value:
            cur.right = self.del_node(cur.right,value)

        return cur


root = TreeNode(2);root.left = TreeNode(1);root.right = TreeNode(4)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)

s = Solution()

print(s.del_node(root,1))




