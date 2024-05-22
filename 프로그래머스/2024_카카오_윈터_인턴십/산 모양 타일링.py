def solution(n, tops):
    tile = [0]* (2*n+2)
    tile[0], tile[1] = 1, 1

    now = 0
    for i in range(2, 2*n+2):
        if i%2 == 0:
            if tops[now] == 0:
                tile[i] = (tile[i-1]+tile[i-2])%10007
            else:
                tile[i] = (tile[i-1]*2+tile[i-2])%10007
            now += 1
        else:
            tile[i] = (tile[i-1] + tile[i-2])%10007

    return tile[2*n+1]