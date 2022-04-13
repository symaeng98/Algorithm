##함수 선언 부분


##변수 선언 부분
cnt = 0
is_right = 0
##메인 함수 부분
if __name__ == "__main__":
    data = int(input())
    i = 1
    while True:
        N = str(i)
        is_right = N.find('666')
        if is_right != -1: #만약 is_right가 -1이면 문자열 안에 '666'이 없다는 뜻이므로
            cnt += 1 #있으면 cnt + 1
        if cnt == data:
            print(i)
            break
        i += 1

##파이썬의 장점인 다양한 함수들을 이용해서 풀어봤다. find함수는 한 글자만이 아니라 문자열도 찾을 수 있다는 것을 배웠다.