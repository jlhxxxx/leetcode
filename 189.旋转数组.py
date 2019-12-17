#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = k % len(nums)
        # nums = nums[-n:] + nums[:-n]
        
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1


