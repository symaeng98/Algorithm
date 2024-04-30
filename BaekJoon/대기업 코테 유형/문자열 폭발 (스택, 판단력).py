word = input()
bomb = input()

length = len(bomb)
result = []
for w in word:
    result.append(w)
    if result[len(result)-length:] == list(bomb):
        for _ in range(length):
            result.pop()

if len(result) == 0:
    print("FRULA")
else:
    print(''.join(result))