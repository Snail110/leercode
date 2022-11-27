"""
1、反转链表
2、按照left和right区间反转

"""
class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None

# class Solution:
#     def reverse_list(self,cur:ListNode):
#         pre = ListNode()
#         while cur:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre
#
#     def print_list(self,cur:ListNode):
#         while cur:
#             print(cur.val)
#             cur = cur.next
#
#     def reverse_index(self,cur:ListNode,left:int,right:int):
#
#         head = cur
#         i = 1
#         pre = ListNode()
#         left_cur = ListNode()
#         next_cur = ListNode()
#         right_cur = ListNode()
#
#         while cur:
#             if i==left-1:
#                 pre = cur
#             left_cur = pre.next
#             if i == right:
#                 right_cur = cur
#             next_cur = right_cur.next
#             i += 1
#             cur = cur.next
#
#         right_cur.next = ListNode()
#
#         self.reverse_list(left_cur)
#
#         pre.next = right_cur
#         left_cur.next = next_cur
#
#         return head

class Solution:
    def print_list(self,cur:ListNode):
        while cur:
            print(cur.val)
            cur = cur.next

    def reverse_index(self,cur:ListNode,left:int,right:int):
        dummy = ListNode()
        dummy.next = cur
        pre = dummy

        for i in range(left):
            pre = pre.next
        cur = pre.next
        # cur一直都是left保持不变，然后不断的将cur下一个节点反转刀pre的下面
        for j in range(right-left):
            next = cur.next # 获取cur的下一个节点 也就是将要跳到前面的节点

            cur.next = next.next # 第一步：cur指向next下一个的节点

            next.next = pre.next # next指向 pre的下一个节点

            pre.next = next # pre将指向跳过来的节点

        return dummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(s.print_list(s.reverse_index(head,2,4)))
