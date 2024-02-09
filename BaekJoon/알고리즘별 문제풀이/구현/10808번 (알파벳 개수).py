word = input()
arr = [0]*26

for s in word:
    arr[ord(s)-97] += 1

for a in arr:
    print(a, end=" ")