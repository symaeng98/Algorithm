arr = list(map(int, input()))
numbers = []
zeros = []
for a in arr:
    if a != 0:
        numbers.append(a)
    else:
        zeros.append(a)

if len(zeros) == 0:
    print(-1)
else:
    if sum(numbers)%3 != 0:
        print(-1)
    else:
        arr.sort(reverse=True)
        for a in arr:
            print(a, end="")