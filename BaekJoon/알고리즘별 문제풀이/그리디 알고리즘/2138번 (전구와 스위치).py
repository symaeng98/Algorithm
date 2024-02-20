import copy

def click(before, after, n):
    cnt = 0
    for i in range(1, n):
        if before[i-1] != after[i-1]:
            cnt += 1
            before[i-1] = 1 - before[i-1]
            before[i] = 1 - before[i]
            if i != n-1:
                before[i+1] = 1 - before[i+1]
    if before == after:
        return cnt
    else:
        return 1e9


n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))
tmp1 = copy.deepcopy(a)
tmp2 = copy.deepcopy(a)


tmp1[0] = 1 - tmp1[0]
tmp1[1] = 1 - tmp1[1]
cnt1 = click(tmp1, b, n)+1

cnt2 = click(tmp2, b, n)

answer = min(cnt1, cnt2)
if answer == 1e9:
    print(-1)
else:
    print(answer)