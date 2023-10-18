s = input()

zeros = 0
ones = 0

for o in s.split("0"):
    if o != '':
        ones += 1

for z in s.split("1"):
    if z != '':
        zeros += 1

if ones > zeros:
    print(zeros)
else:
    print(ones)