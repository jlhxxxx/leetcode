#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.88%)
# Total Accepted:    44.9K
# Total Submissions: 102.9K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # temp = out = nums[0]
        # for i in nums[1:]:
        #     if temp > 0:
        #         if temp + i > 0:
        #             temp += i
        #         else:
        #             temp = 0
        #     else:
        #         temp = i

        #     if temp > out:
        #         out = temp
        # return out
        if not nums:
            return 0
        temp = out = nums[0]
        for n in nums[1:]:
            temp = max(n, temp+n)
            out = max(temp, out)
        return out


        
