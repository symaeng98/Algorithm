n = int(input())

result = 0

painkiller = n // 14
n %= 14

medicine = n // 7
n %= 7

print(painkiller + medicine + n)