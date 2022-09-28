"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    # 输入为链表head，n为删除的倒数的节点
    def delNNode(self,head:ListNode,n:int):
        head_dummy = ListNode() # 定义一个虚拟链表节点
        head_dummy.next = head # 指向输入的head
        fast,slow = head_dummy,head_dummy # 定义初始节点指向虚拟节点
        while(n>0 and fast != None):
            fast = fast.next # 移动节点
            n -= 1
        # fast 下一个一个节点不为None
        while(fast.next!=None):
            fast = fast.next
            slow = slow.next
        # fast走到末尾，low走到了倒数n节点前一个
        slow.next = slow.next.next
        # 返回应该为head 节点的头部
        return head_dummy.next


