"""
1. 问题描述：

在河上有一座独木桥，一只青蛙想沿着独木桥从河的一侧跳到另一侧。在桥上有一些石子，青蛙很讨厌踩在这些石子上。由于桥的长度和青蛙一次跳过的距离都是正整数，我们可以把独木桥上青蛙可能到达的点看成数轴上的一串整点：0，1，……，L（其中L是桥的长度）。坐标为0的点表示桥的起点，坐标为L的点表示桥的终点。青蛙从桥的起点开始，不停的向终点方向跳跃。一次跳跃的距离是S到T之间的任意正整数（包括S,T）。当青蛙跳到或跳过坐标为L的点时，就算青蛙已经跳出了独木桥。题目给出独木桥的长度L，青蛙跳跃的距离范围S,T，桥上石子的位置。你的任务是确定青蛙要想过河，最少需要踩到的石子数。

输入格式

第一行有一个正整数L（1 <= L <= 10^9），表示独木桥的长度。第二行有三个正整数S，T，M，分别表示青蛙一次跳跃的最小距离，最大距离，及桥上石子的个数，其中1 <= S <= T <= 10，1 <= M <= 100。
第三行有M个不同的正整数分别表示这M个石子在数轴上的位置（数据保证桥的起点和终点处没有石子）。所有相邻的整数之间用一个空格隔开。

输出格式

输出格式 只包括一个整数，表示青蛙过河最少需要踩到的石子数。


样例输入

10
2 3 5
2 3 5 6 7

样例输出

2

[数据规模】 对于30%的数据，L <= 10000； 对于全部的数据，L <= 10^9。

动态规划问题：
1.init dp[i]表示 在i位置最少需要踩到的石子数量
2.递推公式
if i-j 属于 [i-S:i-T]之间 and stone[i-j] = 1 那么 dp[i] = min(dp[i],dp[i-j])
else: dp[i] = min(dp[i],dp[i-j])

3.初始化
dp = [sys.maxsize] * L
dp[0] = 0
4.遍历顺序
for i in range(1,L):
    for j in range(S,T+1):
        # 无法通过上一个步骤到达当前的i位置则break
        if i-j < 0:
            break
        elif dp[i - j] != sys.maxsize:
            if stone[j] == 1:
                dp[i] = min(dp[i],dp[i-j] + 1)
            else:
                dp[i] = min(dp[i],dp[i-j])

一个很简单的线性dp。
很容易想到dp[i]表示跳到了位置i踩到的石子最少dp[i]表示跳到了位置i踩到的石子最少
容易得到转移方程

dp[i]=min(dp[i],dp[i-j]+vis[i-j])

其中i≥j、 s≤j≤t、vis[i]表示i位置是否有石头其中i≥j、s≤j≤t、vis[i]表示i位置是否有石头

然后看到L是1e9 直接螺旋升天

然后可以发现除了L之外，s、t、m的范围都很小，提示的简直不要太明显(快从这里入手)
这些范围小说明什么？
一、石子个数很少。
二、相邻的石子之间的距离可能相隔很远，不是一步内能跳到的。
假设a和b是相邻的石子，距离为d，且d＞t，一步内到不了。
可以发现如果d＞t，那么任意的距离都可以表示为d%t+t
比如要从1跳到20 s=1、t=3
那么跳到20等价跳到17 14 11 8 5 2
跳到2 在跳6个3到20

跳到19等价跳到 16 13 10 7 4
跳到4 再跳5个3到19

跳到18等价跳到 15 12 9 6 3
跳到3 在跳5个3到18

等于跳的距离可以映射到[1,t+t-1]之间
也就是先跳一个固定距离，然后一直跳t即可
那么10^9的长度就能用2 * t * m的距离表示出来了。
处理出来所有的有石子的新位置去dp。
还有一点要注意的，终点是只要≥l即可，而不是一定要在l那一点上，所以要往后去找最小值

"""

import sys

if __name__ == "__main__":
    # L = 100
    # S, T, M = 2, 3, 5
    # stone_pos = [0, 2, 3, 5, 11,12,13,15, L]

    L = int(input()) # 桥长度
    S,T,M = map(int,input().split()) # S T代表跳跃区间，M代表石头个数
    stone_pos = list(map(int,input().split())) # stone_pos代表位置
    # 对石头位置进行排序
    stone_pos = sorted(stone_pos)
    # 添加0位置和最后的一个位置
    stone_pos = [0] + stone_pos + [L]
    v = [0] * 2005
    cnt = 0
    # 缩短石头距离
    for i in range(1,M+2):
        if stone_pos[i] - stone_pos[i-1] > T:
            # 取模后再+T
            cnt += (stone_pos[i] - stone_pos[i-1]) % T + T
        else:
            cnt += stone_pos[i] - stone_pos[i - 1]
        # 新的石头位置
        v[cnt] = 1
    # 对于最后石头设置为0，初始位置也为0
    v[cnt] = 0
    v[0] = 0
    # init 初始值为最大
    dp = [sys.maxsize] * 2005
    # 0位置为0
    dp[0] = 0
    # 遍历从1开始，然后遍历到跳到最大位置即 cnt + T
    for i in range(1,cnt+T+1):
        # 遍历 j 必须在ST之间，
        for j in range(S,T+1):
            # 当i-j大于0，那么满足跳条件
            if i - j >= 0:
                # dp[i]依赖dpi-j],并且当v[i]有石头就+1，没有+0
                dp[i] = min(dp[i],dp[i-j] + v[i])
    res = sys.maxsize
    # 最后因为重要跳出来就行，因此找到cnt之后的最小值
    for i in range(cnt,cnt+T+1):
        res = min(res,dp[i])
    print(res)





