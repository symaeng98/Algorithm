n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0

cnt_list = [0]*(max(arr)+1)
answer = 0
while right < n:
    if cnt_list[arr[right]] < k:
        cnt_list[arr[right]] += 1
        right += 1
    else:
        cnt_list[arr[left]] -= 1
        left += 1

    answer = max(answer, right-left)

print(answer)