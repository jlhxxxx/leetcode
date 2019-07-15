#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 0
        while n > 0:
            m = n//5
            i = i + m
            n = m
        return i

        

