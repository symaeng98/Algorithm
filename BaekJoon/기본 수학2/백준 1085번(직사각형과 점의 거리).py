##함수 선언 부분


##변수 선언 부분
min = 0
list_t = []
##메인 함수 부분
if __name__ == "__main__":
    list_t = [x for x in map(int,input().split())]
    list_t[2] = list_t[2] - list_t[0] #w - x입력
    list_t[3] = list_t[3] - list_t[1] #h - y입력
    list_t.sort() #오름차순 정렬
    print(list_t[0]) #출력


##개념만 물어보는 문제다