# -1 1 2 3
# - 개수 짝수 -> -랑 + 따로 계산
# - 개수 홀수 -> 남은 -1, -2, -3, -4, -5

n = int(input())

minus_arr = []
plus_arr = []
for _ in range(n):
    x = int(input())
    if x <= 0:
        minus_arr.append(x)
    else:
        plus_arr.append(x)

minus_arr.sort()
plus_arr.sort(reverse=True)

result = 0
left_plus = 0
for i in range(0, len(plus_arr), 2):
    if len(plus_arr[i:]) == 1:
        left_plus = plus_arr[i]
        break
    if plus_arr[i] == 1 or plus_arr[i+1] == 1:
        result += plus_arr[i] + plus_arr[i+1]
        continue
    result += plus_arr[i] * plus_arr[i+1]

left_minus = 0
for i in range(0, len(minus_arr), 2):
    if len(minus_arr[i:]) == 1:
        left_minus = minus_arr[i]
        break
    result += minus_arr[i] * minus_arr[i+1]


print(result+left_plus+left_minus)
