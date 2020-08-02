#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        p1 = self.helper(nums[:-1])
        p2 = self.helper(nums[1:])
        return max(p1,p2)

    def helper(self,nums):
        cur,pre = 0,0
        for num in nums:
            cur,pre = max(pre+num,cur),cur
        return cur






# @lc code=end

