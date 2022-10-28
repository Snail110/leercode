"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def FindNode(self,headA:ListNode,headB:ListNode):
        curA = headA
        curB = headB
        # 根据快慢指总会相遇原则，相遇即可交点
        # 一直循环，直到相较
        while(curA !=curB):
            # 如果curA==None，说明curA走完了，那么将curA赋值为headB
            if(curA):
                curA = headB
            else:
                curA = curA.next
            if (curB):
                curB = headA
            else:
                curB= curB.next
        return curA

