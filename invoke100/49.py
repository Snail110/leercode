import collections
class Solution:
    def groupAnagrams(self,strs):
        mp = collections.defaultdict(list)
        
        for st in strs:
            counts = [0] * 26
            for s in st:
                num = ord(s) - ord('a')
                counts[num] += 1
            mp[tuple(counts)].append(st)
        
        return list(mp.values())

s = Solution()
strs = ['eat','tea','tan','ate','nat','bat']
print(s.groupAnagrams(strs))