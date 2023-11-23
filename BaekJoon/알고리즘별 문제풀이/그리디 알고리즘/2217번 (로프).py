n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

max_value = ropes[0]

for k in range(2, len(ropes)+1):
    max_value = max(max_value, ropes[k-1]*k)

print(max_value)