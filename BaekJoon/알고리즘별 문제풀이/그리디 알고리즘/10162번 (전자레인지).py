time = int(input())

count = [0]*3

five_minute_count = time // 300
time -= 300*five_minute_count
count[0] += five_minute_count


one_minute_count = time // 60
time -= 60*one_minute_count
count[1] += one_minute_count

ten_seconds_count = time // 10
time -= 10*ten_seconds_count
count[2] += ten_seconds_count

if time != 0:
    print(-1)
else:
    for c in count:
        print(c, end=" ")