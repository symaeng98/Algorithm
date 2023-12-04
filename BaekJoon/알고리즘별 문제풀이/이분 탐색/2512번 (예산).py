n = int(input())
cities = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(cities)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for city in cities:
        if city > mid:
            total += mid
        else:
            total += city
    if total <= budget:
        start = mid+1
    else:
        end = mid-1

print(end)