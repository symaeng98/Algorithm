from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        cnt_dict = defaultdict(int)
        for mag_alpha in magazine:
            cnt_dict[mag_alpha] += 1

        for ran_alpha in ransomNote:
            if cnt_dict[ran_alpha] == 0:
                return False
            cnt_dict[ran_alpha] -= 1
        return True