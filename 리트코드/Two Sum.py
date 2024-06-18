class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in num_dict:
                return [num_dict[x], i]
            num_dict[nums[i]] = i