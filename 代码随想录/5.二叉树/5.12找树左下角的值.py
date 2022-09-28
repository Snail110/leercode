"""
找树左下角的值
层序遍历

如果需要遍历整棵树，递归函数就不能有返回值。如果需要遍历某一条固定路线，递归函数就一定要有返回值！

"""

from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def leftNodeValue(self,root:TreeNode):
        """
        层序遍历
        :param root:
        :return: result int
        """
        if root != None:
            # 初始节点
            q = deque([root])
        result = 0
        while(q):
            # 统计deque的长度
            size = len(q)
            for i in range(size):
                # 依次弹出最前面的值
                front = q.popleft()
                # 记录第一个值也就是最左边的值
                if(i==0):
                    result = front.value
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

        return result

root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(4);root.left.right = TreeNode(1)

root.left.left.left = TreeNode(1)


s = Solution()
print(s.leftNodeValue(root))