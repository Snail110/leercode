"""

"""


def extend(s, i, j, n):
    res = 0
    while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1
        res += 1
    return res

s = 'bab'

print(extend(s,1,1,3))