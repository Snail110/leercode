"""
采用pre的前指针记录重复的值，并且通过res=[] 记录最大重复的value和节点，采用count 记录重复次数

"""
class TreeNode:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.res = []

    def Bsf(self, cur:TreeNode):
        if cur is None:
            return

        # 左
        self.Bsf(cur.left)
        # 中'
        if self.pre.value == cur.value:
            self.count += 1
        else:
            self.count = 1

        if self.max_count == self.count:
            self.res.append(cur.value)
        if self.max_count < self.count:
            self.res = []
            self.res.append(cur.value)
            self.max_count = self.count

        # 右
        self.pre = cur
        self.Bsf(cur.right)


    def getMode(self,root:TreeNode):
        if root is None:
            return []
        self.Bsf(root)

        return self.res

root = TreeNode(2);root.left = TreeNode(1);root.right = TreeNode(3)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)

s = Solution()

print(s.getMode(root))

res = [1,2,3,3,7]