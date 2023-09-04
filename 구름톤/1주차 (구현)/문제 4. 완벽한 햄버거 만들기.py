n = int(input())
hamburger = list(map(int, input().split()))

max_index = hamburger.index(max(hamburger))
left = hamburger[:max_index]
right = hamburger[max_index:]

isPerfect = True
for i in range(0, len(left)-1):
    if left[i] > left[i+1]:
        isPerfect = False
        break

for i in range(0, len(right)-1):
    if right[i] < right[i+1]:
        isPerfect = False
        break

if isPerfect:
    print(sum(hamburger))
else:
    print(0)