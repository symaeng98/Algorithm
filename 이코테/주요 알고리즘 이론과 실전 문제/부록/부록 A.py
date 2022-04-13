##round() 함수 -> 반올림
a = 0.3 + 0.6
print(round(a,4))


##집합 초기화 방법
data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)


##집합 자료형의 연산
a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a|b)
print(a&b)
print(a-b)


##집합 자료형 관련 함수
data = set([1,2,3])
print(data)

data.add(4)
print(data)

data.update([5,6])
print(data)

data.remove(3)
print(data)

##f-string
answer = 7
print(f"정답은 {answer} 입니다")


##기본 내장 함수
result = sum([1,2,3,4,5])
print(result)

result = eval("(3+5)*7")
print(result)

result = sorted([9,1,8,5,4])
print(result)
result = sorted([9,1,8,5,4],reverse=True)
print(result)

result = sorted([('홍길동',35),('이순신',75),('아무개',50)],
                key=lambda x:x[1],reverse=True)
print(result)

data = [9,1,8,5,4]
data.sort()
print(data)

##itertools
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))
print(result)

from itertools import product
data = ['A','B','C']
result = list(product(data,repeat=2))
print(result)

from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)

##heapq
import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)



##bisect
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a,x))
print(bisect_right(a,x))

from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

##collections
from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))