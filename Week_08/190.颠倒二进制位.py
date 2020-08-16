#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res,power = 0,31
        while n:
            res += (n&1)<<power
            n = n>>1
            power -= 1
        return res
        
# @lc code=end

