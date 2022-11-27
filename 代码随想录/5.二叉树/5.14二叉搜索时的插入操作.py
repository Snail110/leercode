"""
二叉搜索树的插入操作，只需要不改变树的结构，在叶子缎插入满足要求的节点即可

"""

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def insert_node(self,cur:TreeNode,value:int):
        """

        :param cur:
        :param value:
        :return:
        """

        # 终止条件 一直遍历到叶子节点
        if cur is None:
            node = TreeNode(value)
            return node

        if value > cur.value:
            cur.right = self.insert_node(cur.right,value)
        else:
            cur.left = self.insert_node(cur.left,value)

        return cur

root = TreeNode(2);root.left = TreeNode(1);root.right = TreeNode(4)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)

s = Solution()

r = s.insert_node(root,8)
print(r.right.right.right.value)
