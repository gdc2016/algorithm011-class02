#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s,counter_t = {},{}
        for i in range(len(s)):
            if s[i] in counter_s:
                counter_s[s[i]] += 1
            else:
                counter_s[s[i]] = 1
            if t[i] in counter_t:
                counter_t[t[i]] += 1
            else:
                counter_t[t[i]] = 1
        return counter_s == counter_t

# @lc code=end

