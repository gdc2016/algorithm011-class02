#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for s in zip(*strs):
            tmp_set = set(s)
            if len(tmp_set) == 1:
                res += s[0]
            else:
                break
        return res
# @lc code=end

