from bisect import bisect_left, bisect_right

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
nums = set(arr)

max_cnt = -1
max_cnt_num = 0
for num in nums:
    cnt = bisect_right(arr, num) - bisect_left(arr, num)
    if max_cnt < cnt:
        max_cnt = cnt
        max_cnt_num = num

print(max_cnt_num)
