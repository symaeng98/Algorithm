t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = []

    cnt = 0
    for a in arr:
        if a%3 != 0:
            continue
        price = (a//3)*4
        for j in range(len(arr)):
            if price == arr[j] and price != 0:
                result.append(a)
                arr[j] = 0
                break
    print(f"#{test_case} ",end="")
    for r in result:
        print(r, end=" ")
    print()
