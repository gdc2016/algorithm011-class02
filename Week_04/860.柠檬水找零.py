#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for money in bills:
            if money == 5:
                five += 1
            elif money == 10:
                five -= 1
                ten += 1
            else:
                if ten >0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0 or ten <0:
                return False
        return True

        
# @lc code=end

