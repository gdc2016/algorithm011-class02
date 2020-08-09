#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(0,0,'',res,n)
        return res

    def helper(self,left,right,s,res,n):
        if left == n and right == n:
            res.append(s)
        if left < n:
            self.helper(left+1,right,s+'(',res,n)
        if right < left:
            self.helper(left,right+1,s+')',res,n)
        


# @lc code=end

