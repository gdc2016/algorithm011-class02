#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums)-1
        for i in range(len(nums)-1,0,-1):
            if i-1 + nums[i-1] >= reach:
                reach = i-1
        return reach == 0



# @lc code=end

