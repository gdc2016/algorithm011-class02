#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1)+1,len(text2)+1
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        
# @lc code=end

