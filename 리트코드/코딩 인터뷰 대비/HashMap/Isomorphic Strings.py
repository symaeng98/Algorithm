from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        mapping_dict = defaultdict(str)
        used_dict = defaultdict(bool)
        for i in range(len(s)):
            if mapping_dict[s[i]]:
                if mapping_dict[s[i]] != t[i]:
                    return False
                else:
                    continue
            if used_dict[t[i]]:
                return False
            mapping_dict[s[i]] = t[i]
            used_dict[t[i]] = True
        return True