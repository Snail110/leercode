"""
sort
"""

def partion(nums,low,high):
    pivot = nums[high]
    index = low - 1
    for i in range(low,high):
        if nums[i] < pivot:
            index += 1
            nums[index],nums[i] = nums[i],nums[index]

    index += 1
    nums[index],nums[high] = nums[high],nums[index]
    return index
def quick_sort(nums,low,high):

    if low < high:
        pi = partion(nums,low,high)
        quick_sort(nums,low,pi-1)
        quick_sort(nums,pi+1,high)

    return nums

nums = [1,3,4,2]
quick_sort(nums,0,len(nums)-1)
print(nums)