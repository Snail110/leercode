class Solution:
    def insert(self,intervals,newIntervals):
        intervals_add = []
        count = 0
        for num in intervals:
            
            if (newIntervals[0] >= num[0] and newIntervals[0] <= num[1]) or (newIntervals[1] >= num[0] and newIntervals[1] <= num[1]):
                newIntervals[0] = min(num[0],newIntervals[0])
                newIntervals[1] = max(num[1],newIntervals[1])
            elif newIntervals[0] > num[1]:
                intervals_add.append(num)
            elif newIntervals[1] < num[0]:
                if count <1:
                    intervals_add.append(newIntervals)
                    count += 1
                intervals_add.append(num)
        
        # 如果全部重叠，需要最后将newIntervals加进去
        if count <1:
            intervals_add.append(newIntervals)
        return intervals_add
s = Solution()
intervals = [[1,3],[6,9]]
newIntervals = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16],[17,18]]
newIntervals = [4,8]
print(s.insert(intervals,newIntervals))            
