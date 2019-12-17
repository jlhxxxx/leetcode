#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (38.31%)
# Total Accepted:    31.9K
# Total Submissions: 81.9K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        m, n = 0, len(s)-1
        while m < n:
            while not s[m].isalnum() and m < n:
                m += 1
            while not s[n].isalnum() and m < n:
                n -= 1
            if s[m].lower() != s[n].lower():
                return False
            m, n = m+1, n-1
        return True 

        
