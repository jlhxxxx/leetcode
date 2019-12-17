#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
from functools import reduce
class Solution:
    def titleToNumber(self, s: str) -> int:
        def f(x, y):
            return 26*x + y

        def ff(x):
            return ord(x) - 64

        return reduce(f, map(ff, s))

        # return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))


