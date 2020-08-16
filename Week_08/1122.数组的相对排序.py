#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0 for _ in range(1001)]
        for i in arr1:
            count[i] += 1
        j = 0
        for i in arr2:
            while count[i] > 0:
                arr1[j] = i
                j += 1
                count[i] -= 1

        for i in range(len(count)):
            while count[i] > 0:
                arr1[j] = i
                j += 1
                count[i] -= 1
        return arr1 
        
# @lc code=end

