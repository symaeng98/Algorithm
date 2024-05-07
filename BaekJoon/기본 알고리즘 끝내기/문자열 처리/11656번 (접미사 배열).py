word = input()
arr = []
for i in range(len(word)):
    arr.append(word[i:])
print('\n'.join(sorted(arr)))