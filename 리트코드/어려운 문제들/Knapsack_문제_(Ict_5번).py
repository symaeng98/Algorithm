# ICT 인턴십 코딩 테스트 5번 문제입니다(해커랭크)
# https://leetcode.com/problems/painting-the-walls/solutions/3994662/painting-the-walls/

INF = 1e9
def dp(i, remain, cost, time, n):
    if remain <= 0:
        return 0
    if i == n:
        return INF

    paint = cost[i] + dp(i + 1, remain - 1 - time[i], cost, time, n)
    dont_paint = dp(i + 1, remain, cost, time, n)
    return min(paint, dont_paint)

def getMinCost(cost, time):
    n = len(cost)

    return dp(0, n, cost, time, n)




print(getMinCost([1,1,3,4], [3,1,2,3]))
print(getMinCost([1,2,3,2], [1,2,3,2]))
print(getMinCost([2,3,4,2], [1,1,1,1]))
print(getMinCost([2,3,4,5,5], [1,1,1,100,30]))