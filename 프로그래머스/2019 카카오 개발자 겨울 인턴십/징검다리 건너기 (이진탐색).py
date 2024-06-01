def solution(stones, k):
    def check(t):
        cnt = 0
        for stone in stones:
            if stone-t <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                return False

        return True

    start = min(stones)
    end = max(stones)
    while start+1 < end:
        mid = (start + end) // 2
        if check(mid):
            start = mid
        else:
            end = mid

    if check(end):
        return end+1
    if check(start):
        return start+1
    else:
        return start
