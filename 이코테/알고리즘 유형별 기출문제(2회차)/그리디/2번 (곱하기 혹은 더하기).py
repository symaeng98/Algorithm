s = input()
result = 0
for i in range(len(s)):
    if result == 0:
        result += int(s[i])
        continue
    if s[i] != "0":
        result = max(result * int(s[i]), result + int(s[i]))

print(result)