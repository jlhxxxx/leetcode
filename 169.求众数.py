#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # countDic = {}
        # for i in nums:
        #     countDic.setdefault(i, 0)
        #     countDic[i] += 1
        # for k, v in countDic.items():
        #     if v >= len(nums)/2:
        #         return k
        
        return sorted(nums)[len(nums)//2]
        

