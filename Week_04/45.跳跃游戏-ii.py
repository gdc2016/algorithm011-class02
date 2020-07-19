#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        pos,step = len(nums)-1,0
        while pos != 0:
            for i in range(pos):
                if i + nums[i] >= pos: 
                    pos = i
                    step += 1
                    break
        return step


            


            


# @lc code=end

