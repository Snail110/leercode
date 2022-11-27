"""
给一个Map,按照value降序输出
"""

class Soluton:
    def sortMap(self,nums:dict):

        sorted(nums.items(), key=lambda item: item[1])
        return nums




s = Soluton()
tinydict = {'a': 1, 'b': 2, 'c': 3}

print(s.sortMap(tinydict))


