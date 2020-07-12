#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res,used = [],[False]*len(nums)
        nums.sort()
        self.helper(nums,[],used,res)
        return res

    def helper(self,nums,temp,used,res):
        if len(temp) == len(nums):
            res.append(temp[:])
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            temp.append(nums[i])
            used[i] = True
            self.helper(nums,temp,used,res)
            temp.pop()
            used[i] = False
        


# @lc code=end

