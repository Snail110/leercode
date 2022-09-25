"""
给10个排序好(从小到大)的数组，每个数组1000个数字，取出所有数组中最小的500个数

方法一：混在一起，排序
方法二：新建一个数组A 500，然后对于每个数组一起从i=0开始比较最小值，放在数组A i=0，然后被选出来最小值的数组不断地的填充，继续比较
知道满500 归并排序 499 * nlogn
方法三：新建一个数组A 500，维护一个小顶堆，每次把最顶端的值放入新数组A中直到满
方法四：维护一个大顶堆节点为10（10个数组）和500长度数组，然后分别将每组的数组0位置开始塞进去，然后迭代大顶堆得到根值为最大值，根值放进数组中，
此时将对应的数组
"""
class Solution:
    def sort1(self,a:list,b:list,n):
        """
        适用于a=[[1,2,3]]，b=[[3,4,5]]的格式
        :param a:
        :param b:
        :param n:
        :return:
        """
        merge_list = []
        a = a[0]
        b = b[0]
        while len(a) > 0 and len(b) > 0 and len(merge_list) < n:
            if a[0] < b[0]:
                merge_list.append(a.pop(0))
            else:
                merge_list.append(b.pop(0))

        while len(a) > 0 and len(merge_list) < n:
            merge_list.append(a.pop(0))
        while len(b) > 0 and len(merge_list) < n:
            merge_list.append(b.pop(0))

        return [merge_list]

    def sort(self,a:list,b:list,n):
        """
        适用于a=[[1,2,3]]，b=[[3,4,5]]的格式
        :param a:
        :param b:
        :param n:
        :return:
        """
        merge_list = []
        a = a
        b = b
        while len(a) > 0 and len(b) > 0 and len(merge_list) < n:
            if a[0] < b[0]:
                merge_list.append(a.pop(0))
            else:
                merge_list.append(b.pop(0))

        while len(a) > 0 and len(merge_list) < n:
            merge_list.append(a.pop(0))
        while len(b) > 0 and len(merge_list) < n:
            merge_list.append(b.pop(0))

        return merge_list
    def minNnums(self,a:list,n:int):

        res = a[0]
        for i in a[1:]:
            res = self.sort(res,i,n)

        return res[:n]
    def mergeSort(self,a:list,n:int):
        if len(a) < 2:
            return a
        mid = len(a) // 2
        left = self.mergeSort(a[:mid],n)
        right = self.mergeSort(a[mid:],n)
        return self.sort1(left,right,n)

s = Solution()

a = [[1,7,9,4],[2,3,6,6],[3,5,8,9]]
print(s.minNnums(a,3))

