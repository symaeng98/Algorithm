##함수 선언 부분
import sys


##변수 선언 부분
data = []
data_sorted = []
N = 0

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    data = [int(x) for x in input().split()]
    data_set = set(data) #중복을 없애준다.
    set_data = list(data_set) #집합 형태이므로 리스트로 바꿔준다.
    set_data.sort() #오름차순 정렬하면 각각의 값의 인덱스가 본인보다 작은 값의 수일 것이다.
    data_dic = {set_data[i] : i for i in range(len(set_data))}
    #for문을 사용하면 N이 클 때 시간복잡도가 너무 크기때문에 딕셔너리를 사용해야한다.
    for i in data:
        print(data_dic[i], end = " ")


##시간 복잡도 때문에 고민을 했는데, 아무리 생각해도 for문을 쓰는 것은 좋지 않을 것 같아서 딕셔너리를 썼다.
##이 문제를 통해 딕셔너리의 대부분의 메서드는 시간복잡도가 O(1)이라는 것을 배웠다.
