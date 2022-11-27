#双指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self,head:ListNode):
        if head == None:
            return None

        pre = None
        cur = head
        while cur != None:
            tmp = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre  # 反转
            pre = cur       # 移动pre
            cur = tmp       # 移动cur
        # 返回pre也就是开头的第一个节点
        return pre

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

s = Solution()
print(s.reverse(head).val)