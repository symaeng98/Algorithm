class Solution(object):
    def isHappy(self, n):
        visited = []
        while True:
            if n == 1:
                return True
            if n in visited:
                return False
            visited.append(n)
            sum_value = 0
            for s in str(n):
                sum_value += int(s)**2
            n = sum_value
            print(visited)
