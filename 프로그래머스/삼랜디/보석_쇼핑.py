# 09:05
from collections import defaultdict
def solution(gems):
    n = len(gems)
    m = len(set(gems))
    gem_set = set()
    gem_count = defaultdict(int)
    result = [1, 1000000]
    left, right = 0, 0
    gem_count[gems[left]] += 1
    gem_set.add(gems[left])
    while left < n and right < n and left <= right:
        if len(gem_set) != m:
            right += 1
            if right >= n:
                break
            gem_count[gems[right]] += 1
            gem_set.add(gems[right])
        else:
            if result[1]-result[0] > right-left:
                result[0] = left+1
                result[1] = right+1
            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                gem_set.remove(gems[left])
            left += 1




    return result