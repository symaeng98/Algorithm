s = input()
start = 0
end = len(s)-1

is_palindrome = True
while start < end:
    if s[start] != s[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print(1)
else:
    print(0)