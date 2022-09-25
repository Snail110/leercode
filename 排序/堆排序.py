"""
堆的基本概念：
堆排序是一高效率的排序算法，复杂度是o(nlogn)，经典的topK算法和小顶堆用于实现优先队列

堆排序是利用堆数据结构所设计的一种排序算法，堆实际是一个完全二叉树结构。
完全二叉树：假设一个二叉树的深度为h，除了第h层外，其他各层（1~h-1）的节点数都达到了最大个数，第h层所有的节点都连续集中在最左边，这就是完全二叉树。

堆氛围大顶堆和小顶堆
符合重要的性质：
小顶堆满足：key[i]<=key[2*i+1] and key[i] <=key[2*i+2]
大顶堆满足：key[i]>=key[2*i+1] and key[i] >=key[2*i+2]
即大顶堆最大元素在根节点，节点一定大于其子节点，反之小顶堆最小元素在根节点，



堆排序基本思想及步骤：

堆排序的基本思想是：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，
这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了

1、将待排序的数组初始化为大顶堆，该过程即建堆。
2、将堆元素与最后一个元素进行交换，除去最后一个元素外可以组建新的大顶堆。
3、由于第二步骤堆顶元素跟最后一个元素交换后，就不是大堆顶了，需要重新建立大顶堆，重复上面的处理流程，知道堆中仅剩下一个元素。


问：此时我们需要把这个完全二叉树构造成一个大顶堆，怎么构造呢？
答：一个很好的方法是遍历二叉树的非叶子节点自下往上的构造大顶堆，针对每个非叶子节点，都跟它的左右子节点比较，把最大的值换到这个子树的父节点。

问：为什么要从非叶子节点开始，而不是从最后一个节点开始？
答：因为叶子节点下面没有子节点了，就没必要操作了。

问：为什么要从下往上而不是从上往下遍历非叶子节点？
答：我们从下面开始遍历调整每个节点成为它左右节点的最大值，那么一直往上的话，最后根节点一定是最大的值；
但是如果我们从上往下，上面满足了大顶堆，下面不满足，调整后，上面可能又不满足了，所以从下往上是最好的方案。

那么我们构造的大顶堆的代码就很明显了
构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点

len = len(arr)
for i in range(len//2-1,-1,-1):
   build_heap() # 遍历针对每个非叶子节点构造大顶堆


"""

class Solution:
    def heapSort(self, nums: list):

        size = len(nums)

        self.build_heap(nums, size)

        for i in range(size-1, -1, -1):
            # 交换最后一个元素与第一个元素后，将第一个元素为最大值放在最后面，继续建立大顶堆
            nums[i], nums[0] = nums[0], nums[i]
            # 只有第一个元素修改了，因此只需要对第一个元素进行大顶堆调整就行，不需要全部调整
            self.adjust_heap(0,nums,i)

        return nums

    def build_heap(self, nums: list, i):
        # 大顶堆的构建
        size = len(nums[:i])
        for i in range(size//2-1, -1, -1):
            self.adjust_heap(i, nums, size)
        return nums

    def adjust_heap(self, index: int, nums: list, l: int):
        left = index * 2 + 1    # 左节点
        right = index * 2 + 2   # 右节点
        father_index = index
        if left < l and nums[left] < nums[father_index]:
            father_index = left

        if right < l and nums[right] < nums[father_index]:
            father_index = right

        if father_index != index:
            # 交换 最大值
            nums[index], nums[father_index] = nums[father_index], nums[index]
            # 那个节点交换了，就对该节点进一步递归，查看该节点下是否满足大顶堆。
            self.adjust_heap(father_index, nums, l)

    def topK(self,nums:list,k:int):
        res = []
        for i in range(k):
            res.append(nums[i])

        self.build_heap(res,k)

        for i in nums[k:]:
            if i > res[0]:
                res[0] = i
                self.adjust_heap(0,res,k)
        return res

nums = [4, 6, 7, 2, 9, 8, 3, 5,2,3,4,5,6,7,44,33,77,88,22,33,99,44,54,22,33,66,776,76,45,632]
s = Solution()
print(s.heapSort(nums))
print(s.topK(nums,10))

"""
堆排序复杂度
时间复杂度， 包括两个方面：

初始化建堆过程时间：O(n)
更改堆元素后重建堆时间：O(nlogn)，循环 n -1 次，每次都是从根节点往下循环查找，所以每一次时间是 logn，总时间：logn(n-1) = nlogn - logn ，所以复杂度是 O(nlogn)
时间复杂度：O(nlogn)
空间复杂度： 因为堆排序是就地排序，空间复杂度为常数：O(1)

堆排序的应用：TopK算法

面试中经常考的一个面试题就是，如果在海量数据中找出最大的100个数字，看到这个问题，可能大家首先会想到的是使用高效排序算法，
比如快排，对这些数据排序，时间复杂度是O(nlogn)，然后取出最大的100个数字。但是如果数据量很大，
一个机器的内存不足以一次过读取这么多数据，就不能使用这个方法了。TopK的经典算法就是使用堆排序了，具体方法是：

维护一个大小为k的小顶堆，依次将数据放入堆中国，当堆的大小满了的时候，只需要将堆顶元素与下一个数比较：
1、如果小于堆顶元素，则直接忽略，比较下一个元素；
2、如果大于堆顶元素，则将当前的堆顶抛弃，并将元素插入堆中，再次维护为小顶堆，
3、遍历完全部数据，topk的元素自然在堆里面。


整个操作中，遍历数组需要O(n)的时间复杂度，每次调整小顶堆的时间复杂度是O(logK)，加起来就是 O(nlogK) 的复杂度，如果 K 远小于 n 的话，
 O(nlogK) 其实就接近于 O(n) 了，甚至会更快，因此也是十分高效的。

"""



