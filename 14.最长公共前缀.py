#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.20%)
# Total Accepted:    57.7K
# Total Submissions: 178.7K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        out = '' 
        for i in range(len(strs[0])):
            out = strs[0][:i + 1]
            for s in strs[1:]:
                if s.startswith(out):
                    continue
                else:
                    return strs[0][:i]
        return out

        # if not strs:
        #     return ''
        # if len(strs) == 1 or strs[0] == '':
        #     return strs[0]

        # count = len(strs[0])
        # for s in strs[1:]:
        #     if len(s) < count:
        #         count = len(s)

        # for i in range(count):
        #     tmp = set([x[:i+1] for x in strs])
        #     if len(tmp) > 1:
        #         return strs[0][:i]
        
        # return strs[0][:count]


