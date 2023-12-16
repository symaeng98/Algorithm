s = list(input())
t = list(input())

while len(t) > len(s):
    if t[-1] == "A":
        t.pop()
        continue
    if t[-1] == "B":
        t.pop()
        t.reverse()

if t == s:
    print(1)
else:
    print(0)