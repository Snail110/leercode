"""
lc 12
"""

class Solution:
    def number_2_roma(self,num:int):
        """

        :param num:
        :return:
        """
        # 按照从大到小建立词典，然后循环依次减去，直到减完为止
        value_symbols = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'Xl',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }

        symbol = ''
        for v in value_symbols:
            while num >= v:
                num -= v
                symbol += value_symbols[v]
            if num == 0:
                break
        return symbol

class Solution2:
    def roma_2_number(self,roma:str):
        """

        :param roma:
        :return:
        """
        symbols_value = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }
        res = 0
        for i in range(len(roma)):
            # 如果为倒数第二，并且前面小于后面的，那么应该减去当前值
            if i < (len(roma)-1) and symbols_value[roma[i]] < symbols_value[roma[i+1]]:
                res -= symbols_value[roma[i]]
            else:
                # 否则应该加当前值
                res += symbols_value[roma[i]]
        return res
s2 = Solution2()
num = 'IX'
print(s2.roma_2_number(num))