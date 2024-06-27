class Solution(object):
    def removeDuplicates(self, nums):
        index = 1
        bef = nums[0]
        for i in range(len(nums)):
            if bef == nums[i]:
                continue
            nums[index] = nums[i]
            bef = nums[i]
            index += 1

        return index