n = input()

def cal(num):
    result = 0
    for i in range(len(num)):
        result += int(num[i])
    return result

length = len(n) // 2
if cal(n[:length]) == cal(n[length:]):
    print("LUCKY")
else:
    print("READY")