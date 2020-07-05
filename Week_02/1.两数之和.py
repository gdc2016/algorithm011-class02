#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,item in enumerate(nums):
            if target-item in dic:
                return [i,dic[target-item]]
            else:
                dic[item] = i
                
        
# @lc code=end

