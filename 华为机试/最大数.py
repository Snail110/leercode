"""
lc 179
给定一组非负整数nums，重新排列每个数顺序，返回组成最大整数

"""
from functools import cmp_to_key

def cmp_sort(a:str,b:str):
    # 判断 a和b那个在前面大，只需要将两者拼接一下就行
    return int(a+b)-int(b+a)

def max_num(nums:list):
    nums_sort = sorted(map(str,nums),key=cmp_to_key(cmp_sort),reverse=True)
    return ''.join(nums_sort if nums_sort[0] !=0 else '0')

nums = [10,2,3,34]

print(max_num(nums))
