n, x = map(int, input().split())
arr = list(map(int, input().split()))

result_list = []
tmp = sum(arr[:x])
result_list.append(tmp)
for i in range(1, n-1):
    start = i
    end = i+x-1
    if end <= n-1:
        tmp = tmp-arr[i-1]+arr[end]
        result_list.append(tmp)
    else:
        break
answer = max(result_list)
if answer == 0:
    print("SAD")
else:
    print(answer)
    print(result_list.count(answer))
