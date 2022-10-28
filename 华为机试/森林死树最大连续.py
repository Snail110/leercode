"""
1，有一排树木，按编号1,2,3.......，总共有m颗树，会死掉n颗，这n颗的编号假如为2,4,6......，现在会给你k颗树去补掉已死的，请问求补完之后，连续树木的最大数量。
例子：
输入


5            有5颗树
2            死掉2颗
2   3        死掉的编号2,3
1            可以补1颗
输出 3

解答：
将坏死的树填充0，转化为求包含k个o的最大连续子数组长度。
用：双指针

"""

class Solution:
    def max_len_nums(self):

        N = int(input())
        S = int(input())
        S_index = list(map(int,input().split()))
        K = int(input())
        # N = 7
        # S = 2
        # S_index = [3,4,6]
        # K = 2

        S_nums = 0
        res = 0
        j = 1

        for i in range(1,N+1):
            if i in S_index:
                S_nums += 1

            while S_nums > K:
                if j in S_index:
                    S_nums -= 1
                j += 1  # 滑动窗口的精髓
            res = max(res, i - j + 1)
        return res

s = Solution()
print(s.max_len_nums())









