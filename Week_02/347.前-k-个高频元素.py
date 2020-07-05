#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collect = {}
        for n in nums:
            if n in collect:
                collect[n] += 1
            else:
                collect[n] = 1
        res = heapq.nlargest(k,collect.keys(),collect.get)
        return res
# @lc code=end

