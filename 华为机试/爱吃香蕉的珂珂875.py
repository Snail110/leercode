"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。

珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

 

示例 1：

输入：piles = [3,6,7,11], h = 8
输出：4
示例 2：

输入：piles = [30,11,23,4,20], h = 5
输出：30
示例 3：

输入：piles = [30,11,23,4,20], h = 6
输出：23

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

二分搜索类型题，典型最大最小问题都是用二分搜索来解决的。
可以想象到只要吃掉香蕉的速度足够大，就可以尽快地在有限时间内吃完香蕉堆，而答案正是要找到足够大的选择中的最小速度。
具体来说，对于区间 [1, INT_MAX]，而满足条件的最小速度为 k，则 [k, INT_MAX] 都可以使得猩猩在 h 小时内吃掉所有香蕉，而 [1, k-1] 则不可以满足条件。
所以可以使用二分搜索找到区间中第一个满足条件的速度即为最小速度。
前面我们将二分搜索的初始区间设置为 left = 1 and right = INT_MAX，但实现上可以将右边界设置为数组的最大值，即 right = max(piles)，这是因为 h 是大于等于数组长度的，所以速度选为 max(piles) 必定满足在 h 小时内吃完香蕉堆的要求。
该类二分搜索题目均是不断缩减区间，再用 check 函数（该函数通常就是枚举）来检查 mid 是否满足条件
————————————————
版权声明：本文为CSDN博主「cheny1li1998」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44705592/article/details/127379824

"""


class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        piles_s = sorted(piles)
        low = 1
        high = piles_s[len(piles_s) - 1]
        while low < high:
            mid = (high + low)//2
            h_ = 0
            for i in range(len(piles_s)):
                 h_ += (piles_s[i] -1) // mid + 1
            if h_ <= h:
                high = mid
            else:
                low = mid + 1
        return low

piles =[30,11,23,4,20]
h = 6
s = Solution()
print(s.minEatingSpeed(piles,h))