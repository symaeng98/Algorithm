def solution(arr, n):
    max_arr = []
    if n == 1:
        print(arr[0])
        return
    max_arr.append(arr[0])
    if n == 2:
        print(arr[0] + arr[1])
        return
    max_arr.append(arr[0]+arr[1])
    if n == 3:
        print(max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2]))
        return
    max_arr.append(max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2]))
    if n == 4:
        print(max((arr[0]+arr[1]+arr[3]),(arr[0]+arr[2]+arr[3]),(arr[1]+arr[2])))
        return
    max_arr.append(max((arr[0]+arr[1]+arr[3]),(arr[0]+arr[2]+arr[3]),(arr[1]+arr[2])))
    for i in range(4, n):
        case1 = max_arr[i-3] + arr[i-1] + arr[i]
        case2 = max_arr[i-2] + arr[i]
        case3 = max_arr[i-4] + arr[i-2] + arr[i-1]
        max_arr.append(max(case1,case2,case3))
    print(max_arr.pop())


n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

solution(arr, n)
