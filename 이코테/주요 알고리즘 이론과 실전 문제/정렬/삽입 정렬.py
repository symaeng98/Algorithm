##함수 선언 부분##
import time
from random import randint
##변수 선언 부분##

##메인 함수 부분##
if __name__ == "__main__":
    ##삽입 정렬##
    array = []
    for _ in range(10000):
        array.append(randint(1,100))

    start_time = time.time()
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
                array[j], array[j-1] = array[j-1], array[j]
            else: #자신보다 비교하는 데이터가 더 작으면
                break #비교 정지
    end_time = time.time()
    print("삽입 정렬 성능 측정 :",end_time-start_time)

    ##기본 라이브러리 sort()##
    array = []
    for _ in range(10000):
        array.append(randint(1, 100))

    start_time = time.time()
    array.sort()
    end_time = time.time()
    print("삽입 정렬 성능 측정 :", end_time - start_time)