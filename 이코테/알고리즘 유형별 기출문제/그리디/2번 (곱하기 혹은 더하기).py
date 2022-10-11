s = input()

sum = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or sum <= 1:
        sum += num
    else:
        sum *= num

print(sum)

## 1일 때도 그냥 곱해버려서 틀렸다. 좀 더 꼼꼼하게 생각하자
