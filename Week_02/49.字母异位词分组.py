#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic,res = {},[]
        for word in strs:
            char = tuple(sorted(word))
            if char in dic:
                dic[char].append(word)
            else:
                dic[char] = [word]
        for wg in dic.values():
            res.append(wg)
        return res


# @lc code=end

