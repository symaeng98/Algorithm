def bs(note, start, end, x):
    while start + 1 < end:
        mid = (start + end) // 2
        if note[mid] == x:
            return True
        elif note[mid] < x:
            start = mid
        else:
            end = mid

    if note[start] == x or note[end] == x:
        return True

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    for num in note2:
        if bs(note1, 0, n-1, num):
            print(1)
        else:
            print(0)