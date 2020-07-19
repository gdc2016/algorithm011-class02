#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        i,j = 0,0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count
# @lc code=end

