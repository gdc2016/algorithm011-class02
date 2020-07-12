#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(n,k,1,[],res)
        return res

    def helper(self,n,k,i,cur,res):
        if len(cur) == k:
            res.append(cur[:])
        for j in range(i,n+1):
            cur.append(j)
            self.helper(n,k,j+1,cur,res)
            cur.pop()


        
# @lc code=end

