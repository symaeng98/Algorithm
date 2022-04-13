##함수 선언 부분
import sys


##변수 선언 부분
data = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    M = N
    while(M != 0): #각 자리수를 배열에 넣어주고
        data.append(M % 10)
        M //= 10
    data.sort() #오름차순 정렬 한 뒤
    for i in range(len(data)-1,-1,-1): #거꾸로 출력
        print(data[i],end="")

##reverse = True를 써서 내림차순 정렬 한 뒤 출력해도 된다.