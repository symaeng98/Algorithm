from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        cnt_dict = defaultdict(int)
        for w in s:
            cnt_dict[w] += 1
        for w in t:
            cnt_dict[w] -= 1

        for cnt in cnt_dict.values():
            if cnt != 0:
                return False
        return True