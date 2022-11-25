"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

思路：链表相交说明相交处出现相同的指针，因此需要找到开端两者并行遍历节点是否相等。

"""

class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None



class Solution:
    def list_same_node(self,A:ListNode,B:ListNode):
        """

        :param A:
        :param B:
        :return:
        """
        # 统计长度
        len_a = 0
        len_b = 0
        # 设置初指针
        dummy_a = A
        dummy_b = B
        # 遍历得到初始值
        while A or B:
            if A:
                len_a += 1
                A = A.next
            if B:
                len_b += 1
                B = B.next

        if len_b > len_a:
            dummy_a,dummy_b = dummy_b,dummy_a
            len_a,len_b = len_b,len_a

        len_diff = len_a - len_b

        for i in range(len_diff):
            dummy_a = dummy_a.next
        for j in range(len_b):
            if dummy_a.val == dummy_b.val:
                return dummy_a.val
            dummy_a = dummy_a.next
            dummy_b = dummy_b.next
        return -1

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
A.next.next.next = ListNode(4)
A.next.next.next.next = ListNode(5)

B = ListNode(-1)
B.next = ListNode(3)
B.next.next = ListNode(3)
B.next.next.next = ListNode(4)

s = Solution()
print(s.list_same_node(A,B))



