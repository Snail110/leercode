"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def swapListNode(self,head:ListNode):
        res = ListNode(next=head) # 定义链表
        pre = res # 定义一个虚拟节点
        # 必须有pre的下一个节点和下下一个节点，2个节点才能交换
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next
            # pre cur post 分别指向3个节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next # 移动2个节点
        return res.next


