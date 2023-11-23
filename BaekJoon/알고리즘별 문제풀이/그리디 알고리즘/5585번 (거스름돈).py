n = int(input())

change = 1000 - n

cnt = 0
if change // 500 > 0:
    x = change//500
    cnt += x
    change -= x*500

if change // 100 > 0:
    x = change//100
    cnt += x
    change -= x*100

if change // 50 > 0:
    x = change//50
    cnt += x
    change -= x*50

if change // 10 > 0:
    x = change//10
    cnt += x
    change -= x*10

if change // 5 > 0:
    x = change//5
    cnt += x
    change -= x*5
cnt += change

print(cnt)

