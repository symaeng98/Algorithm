n = int(input())
m = int(input())
buttons = []
if m != 0:
    buttons = list(map(int, input().split()))
f_num_s = ''.join(map(str, buttons))

start = 100

now_cnt = 1e9
now_num = 0
for channel in range(0, 1000001):
    flag = False
    for sc in str(channel):
        if sc in f_num_s:
            flag = True
            break
    if flag:
        continue
    if now_cnt > abs(n-channel):
        now_cnt = abs(n-channel)
        now_num = channel

print(min(abs(n-start), len(str(now_num))+now_cnt))