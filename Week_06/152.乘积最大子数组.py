#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        preMax,preMin = nums[0],nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp1,temp2 = preMax*nums[i],preMin*nums[i]
            preMax = max(temp1,temp2,nums[i])
            preMin = min(temp1,temp2,nums[i])
            res = max(res,preMax)
        return res

# @lc code=end

