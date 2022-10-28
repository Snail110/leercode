'''
题意：反转一个单链表。

示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
#
思路
'''
class ListNode:
    def __init__(self,val=0,mext=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self,head: ListNode):
        cur = head
        pre = None
        # 直到cur为空节点，pre为尾部节点
        while(cur):
            tmp = cur.next # 保存下一个节点
            cur.next = pre # 将下一个节点指向前面
            pre = cur # 移动前一个节点为当前节点
            cur = tmp # 移动当前节点为下一个节点
        # 返回尾部节点pre
        return pre
