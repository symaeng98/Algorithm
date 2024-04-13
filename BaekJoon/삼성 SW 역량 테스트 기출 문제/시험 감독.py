n = int(input())
test_room = list(map(int, input().split()))
a, b = map(int, input().split())

result = len(test_room)
for i in range(len(test_room)):
    test_room[i] -= a

for i in range(len(test_room)):
    if test_room[i] > 0:
        result += ((test_room[i]-1)//b+1)

print(result)