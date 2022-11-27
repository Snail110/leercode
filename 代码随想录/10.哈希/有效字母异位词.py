"""
单词字母相同，但是位置不同
"""
class Solution:
    def word_same(self,a:str,b:str):
        """

        :param a:
        :param b:
        :return:
        """
        if len(a) != len(b):
            return False
        a_map = {}
        len_a = len(a)
        for i in range(len_a):
            if a[i] not in a_map:
                a_map[a[i]] = 1
            else:
                a_map[a[i]] += 1
            if b[i] not in a_map:
                a_map[b[i]] = -1
            else:
                a_map[b[i]] -= 1
        for i in a_map:
            if a_map[i] != 0:
                return False
        return True

a = 'abcd'
b = 'acbd'
s = Solution()
print(s.word_same(a,b))



