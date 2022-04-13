##함수 선언 부분##


##변수 선언 부분##
road = []
price = []
road_sum = 0
sum = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    road = [int(x) for x in input().split()]
    price = [int(x) for x in input().split()]
    min = price[0] #첫 도시의 가격을 최솟값으로 지정
    for i in range(N-1): #N-1번만큼 반복
        if min > price[i] : #가격이 최소인 도시보다 더 싸면
            sum += road_sum * min #이전까지 더한 도로의 길이x가격 을 더해준다.
            road_sum = road[i] #최소인 도시의 road로 초기화
            min = price[i] #가격 갱신
            continue
        road_sum += road[i]
    sum += road_sum * min #마지막 항을 시행하지 않기 때문에 한번 더 계산

    print(sum)