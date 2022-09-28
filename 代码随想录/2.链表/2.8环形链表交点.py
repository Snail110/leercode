"""
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。
"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def findCycleNode(self,head:ListNode):
        fast,slow = head,head
        # 如果fast.next=None，那么就不存在环了，
        while fast and fast.next:
            fast = fast.next.next # 快指针走2步
            slow = slow.next # 慢指针走1步
            if fast==slow:
                # 如果快慢指针相遇，那么重新从相遇q指针从相遇节点开始走，p指针从头开始走
                q = fast
                p = head
                while q!=p:
                    q = q.next
                    p = p.next
                return p
        return None
