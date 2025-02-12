n = int(input())

tmp = [True] * (n + 1)
tmp[0], tmp[1] = False, False

primes = []
for i in range(2, n+1):
    cnt = 2
    if tmp[i]:
        primes.append(i)
        while i*cnt <= n:
            tmp[i * cnt] = False
            cnt += 1

result = 0
left, right = 0, 0
# print(primes)
while right <= len(primes):
    sum_value = sum(primes[left:right])
    if sum_value == n:
        result += 1
        left += 1
        right += 1
    elif sum_value < n:
        right += 1
    else:
        left += 1

print(result)
