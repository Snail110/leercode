"""
**Problem Description**
Given an array of size n that has the following speciﬁcations:
Each element in the array contains either a monkey or a banana.
Each monkey can eat only one banana.
A monkey cannot eat a banana which is more than K units away from the monkey.
We need to ﬁnd the maximum number of bananas that can be eaten by monkeys.
<<<<<<< HEAD


**Input**
Two lines.
The first line contains an array of size n contain chars 'B' (represent Banana) or 'M' (represent Monkey). n >= 0.
The second line contains a integer K, K >= 0.

=======
————————————————
版权声明：本文为CSDN博主「Chauncy__xu」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_44384577/article/details/103290378
>>>>>>> 2f79d352660376dbd55d1aefd708c4dce476a23f
**Input**
Two lines.
The first line contains an array of size n contain chars 'B' (represent Banana) or 'M' (represent Monkey). n >= 0.
The second line contains a integer K, K >= 0.

<<<<<<< HEAD
因为题目要求了一个香蕉最多只能让一个猴子吃，一个猴子也最多吃一个香蕉，因此我们采用投票法的思想，即一个猴子如果吃到了香蕉，我们就把猴子由"M"变成"A",也就是这个猴子吃完一个香蕉之后就再也不能吃香蕉了。
  具体的做法是首先遍历整个MB数组，如果这个数组元素是"B"，则以这个"B"为圆心，以k为半径，1为步长，搜索"M"，如果这个范围内找到"M",则把这个"M"变成"A",跳出循环体，进行下一个循环。
————————————————
版权声明：本文为CSDN博主「Chauncy__xu」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_44384577/article/details/103290378

"""




=======
**Output**
An integer, the maximum number of bananas can be eaten by monkeys

"""

if __name__ == "__main__":

    def main():
        MB = input()
        MB_list = list(MB)
        K = int(input())

        len_MB = len(MB_list)
        E = 0
        for i in range(len_MB):
            if MB_list[i] == 'B':
                for j in range(i-K,i+K,1):
                    if j >= 0 and j < (len_MB - 1) and MB_list[j] == "M":
                        MB_list[j] = 'A'
                        E += 1
                        break
        return E

print(main())
>>>>>>> 2f79d352660376dbd55d1aefd708c4dce476a23f
