#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums,res,[])
        return res

    def helper(self,nums,res,temp):
        if len(temp) == len(nums):
            res.append(temp[:])
        for j in range(len(nums)):
            if nums[j] not in temp:
                temp.append(nums[j])
                self.helper(nums,res,temp)
                temp.pop()

# @lc code=end

