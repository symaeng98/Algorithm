class Solution(object):
    def isPalindrome(self, s):
        def remove(x):
            x = x.lower()
            result = ""
            for k in x:
                ok = ord(k)
                if 48 <= ok <= 57 or 65 <= ok <= 90 or 97 <= ok <= 122:
                    result += k
            return result

        new_s = remove(s)
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[len(new_s)-i-1]:
                return False
        return True
