"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例: 输入："23" 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明：尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

#思路

"""
class Solution:
    def __init__(self):
        self.num_list = ['',
                         '',
                         'abc',
                         'def',
                         'ghi',
                         'jkl',
                         'mno',
                         'pqrs',
                         'yuv',
                         'wxyz']
    def backtracking(self,num_str:str,result:list,path:str,index:int):
        """
        回溯
        :param num_str:
        :param result:
        :param path:
        :param index:
        :return: result
        """
        # 终止条件 当遍历穷尽后的下一层时
        if index == len(num_str):
            result.append(path)
            return

        # 单层逻辑
        num_list_index = ord(num_str[index]) - ord('0')

        for i in range(len(self.num_list[num_list_index])):
            # 处理节点
            path = path + self.num_list[num_list_index][i]
            index = index + 1
            self.backtracking(num_str,result,path,index)
            path = path[:-1]
            index = index - 1

    def joinNumber(self,num_str:str):
        path = ''
        result = []
        index = 0
        self.backtracking(num_str,result,path,index)
        return result

num_str = '234'
s = Solution()
print(s.joinNumber(num_str))
