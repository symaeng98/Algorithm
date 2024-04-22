s = list(input())
t = list(input())

def dfs(x):
    if len(x) == len(s):
        if x == s:
            return True
        return False

    if x[-1] == "A":
        x.pop()
        if dfs(x):
            return True
        x.append("A")
    if x[0] == "B":
        x.reverse()
        x.pop()
        if dfs(x):
            return True
        x.append("B")
        x.reverse()
    return False

if dfs(t):
    print(1)
else:
    print(0)