def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0];
    elif size == 2:
        return max(sticker[0], sticker[1])

    dp1 = [0]*(size-1)
    dp1[0] = sticker[0];
    dp1[1] = sticker[0];

    for i in range(2, size-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])

    dp2 = [0]*size
    dp2[1] = sticker[1];
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])

    return max(dp1[-1], dp2[-1])