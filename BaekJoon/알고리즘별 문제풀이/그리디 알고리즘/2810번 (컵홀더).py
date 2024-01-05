n = int(input())
s = input()
arr = list("E".join(s.replace("LL", "K")))
arr.insert(0, "E")
arr.append("E")
cnt = 0
for i in range(len(arr)):
    if arr[i] == "S":
        if arr[i-1] == "E":
            cnt += 1
            arr[i-1] = "F"
            continue
        if arr[i+1] == "E":
            cnt += 1
            arr[i+1] = "F"
    elif arr[i] == "K":
        if arr[i-1] == "E":
            cnt += 1
            arr[i-1] = "F"
        if arr[i+1] == "E":
            cnt += 1
            arr[i+1] = "F"

print(cnt)