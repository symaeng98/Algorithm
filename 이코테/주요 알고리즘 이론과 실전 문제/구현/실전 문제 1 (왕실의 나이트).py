loc = input()
row = int(loc[1])
col = int(ord(loc[0])) - int(ord('a')) + 1


move = [(2,1), (2,-1), (1,2), (-1,2), (-2,-1), (-2,1), (-1,-2), (1,-2)]

cnt = 0
for m in move:
    if (row + m[0] > 8) or (row + m[0] < 1) or (col + m[1] > 8) or (col + m[1] < 1):
        continue
    cnt += 1

print(cnt)
