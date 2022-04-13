##변수 선언 부분##
Str = []
Newstr = []
##메인 함수 부분##
if __name__ == "__main__":
    Str = input()
    Newstr = Str.split()  ##공백으로 나눠주는 split 함수
    print("%d" % len(Newstr))

##파이썬의 힘을 몸소 느낀 문제
##C언어로 풀었다면 포인터를 이용해서 공백개수세면서 풀었을 것 같다.