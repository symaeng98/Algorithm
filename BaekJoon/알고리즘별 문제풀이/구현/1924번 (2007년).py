month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int, input().split())
month_dif = x - 1
day_dif = y - 1

total_day_dif = 0
for i in range(0, month_dif):
    total_day_dif += month_day[i]
total_day_dif += day_dif

print(res[total_day_dif%7])