class Solution(object):
    def longestCommonPrefix(self, strs):
        result = strs[0]
        for i in range(1, len(strs)):
            index = 0
            for j in range(min(len(result), len(strs[i]))):
                if result[j] != strs[i][j]:
                    break
                index = j+1
            result = result[:index]
        return result
