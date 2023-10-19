from itertools import permutations

def calculate(num_arr, cal_arr):
    sum_value = num_arr[0]
    length = len(cal_arr)
    for i in range(length):
        if cal_arr[i] == "+":
            sum_value += num_arr[i+1]
        elif cal_arr[i] == "-":
            sum_value -= num_arr[i+1]
        elif cal_arr[i] == "x":
            sum_value *= num_arr[i+1]
        else:
            if (num_arr[i+1] > 0 and sum_value > 0) or (num_arr[i+1] < 0 and sum_value < 0):
                sum_value = sum_value // num_arr[i+1]
            else:
                tmp = abs(sum_value)//abs(num_arr[i+1])
                sum_value = -tmp
    return sum_value

n = int(input())
numbers = list(map(int, input().split()))

# + - x /
cal_arr = []
cal_cnt = list(map(int, input().split()))

max_result = -10000000000
min_result = 10000000000
for i,c in enumerate(cal_cnt):
    if i == 0:
        cal = "+"
    elif i == 1:
        cal = "-"
    elif i == 2:
        cal = "x"
    else:
        cal = "/"
    for j in range(cal_cnt[i]):
        cal_arr.append(cal)

for p in permutations(cal_arr,n-1):
    result = calculate(numbers, p)
    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result

print(max_result)
print(min_result)