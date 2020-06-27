# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = sorted(nums)
        i,j = 0,len(temp)-1
        while i < j:
            if temp[i] + temp[j] < target:
                i += 1
            elif temp[i] + temp[j] > target:
                j -= 1
            else:
                # 找到初始数组中这两个数对应的索引，需注意重复值的情况（值相同但是索引不同）
                p = nums.index(temp[i])
                nums.pop(p)
                q = nums.index(temp[j])
                if q >= p:
                    q += 1
                return [p,q]
# leetcode submit region end(Prohibit modification and deletion)
