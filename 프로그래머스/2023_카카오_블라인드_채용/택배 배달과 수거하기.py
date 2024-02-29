def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_cnt = 0
    pickup_cnt = 0

    for i in range(n-1, -1, -1):
        deliver_cnt += deliveries[i]
        pickup_cnt += pickups[i]

        while True:
            if deliver_cnt <= 0 and pickup_cnt <= 0:
                break
            deliver_cnt -= cap
            pickup_cnt -= cap
            answer += (i+1) * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(3, 5, [0, 0, 0, 0, 0], [1, 2, 3, 4, 7]))
