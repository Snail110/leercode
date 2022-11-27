# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
class Solution:
    def replaceListNode(self, head : ListNode, val : int):
        dummy = ListNode(next=head)  # 添加一个虚拟节点
        cull = dummy
        while cull.next!=None:
            if cull.next.val == val:
                cull.next = cull.next.next  # 指向下一个节点
            else:
                cull = cull.next
        return dummy.next

