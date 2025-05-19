class Solution:
    def merge(self, intervals):
        ans = []
        intervals = intervals.sort(key=lambda x:x[0])
        ans.append(intervals[0])
        for num in intervals[1:]:
            if num[0] > ans[-1][-1]:
                ans.append(num)
            elif num[0] > ans[-1][0] and num[0] < ans[-1][-1]:
                ans[-1][-1] = num[-1]
            
        return ans
s = Solution()
intervals = [[1,3],[15,16],[2,6],[8,10]]
print(s.merge(intervals))
