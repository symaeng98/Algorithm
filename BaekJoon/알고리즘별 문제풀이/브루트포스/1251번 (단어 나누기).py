s = list(input())
length = len(s)

min_x = s
result = []
for first in range(1, length-1):
    for second in range(first, length-1):
        a = s[:first]
        b = s[first:second+1]
        c = s[second+1:]

        a.reverse()
        b.reverse()
        c.reverse()

        result.append(''.join(a+b+c))

result.sort()

print(result[0])