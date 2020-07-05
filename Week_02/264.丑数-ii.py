#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
from heapq import heappop,heappush
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap,res = [],0
        heappush(heap,1)
        for _ in range(n):
            res = heappop(heap)
            while heap and res == heap[0]:
                res = heappop(heap)
            for num in [2,3,5]:
                heappush(heap,res*num)
        return res
# @lc code=end

