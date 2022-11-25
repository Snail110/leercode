"""
题意：删除链表中等于给定值 val 的所有节点。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]

"""

class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class Solution:
    def remove_val(self,cur:ListNode,val:int):
        # 设置虚拟头
        dummy = ListNode()
        dummy.next = cur
        pre = dummy
        while pre.next:
            if pre.next.val == val:
                # 如果相等，那么就将next链接到下下一个位置
                pre.next = pre.next.next
            else:
                # 否则就正常更新pre
                pre = pre.next
        # 最终返回dummy虚拟节点的下个节点
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next = ListNode(5)
s = Solution()
print(s.remove_val(head,3).val)