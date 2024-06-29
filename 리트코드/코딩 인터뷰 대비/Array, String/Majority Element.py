class Solution(object):
    def majorityElement(self, nums):
        cnt, result = 0, 0
        for i in range(len(nums)):
            if cnt == 0:
                result = nums[i]
            if result == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return result