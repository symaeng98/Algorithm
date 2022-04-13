##함수 선언 부분##

##변수 선언 부분##
height = 0
up = 0
down = 0
dn = 0
day = 0
##메인 함수 부분##
if __name__ == "__main__" :
    up, down, height = map(int, input().split())
    dn = up - down ##하루에 달팽이가 가는 길이
    if (height -up) % dn == 0: ##마지막엔 up만큼 올라가서 끝나기 때문에 그만큼 빼준다.
        day = 0
    else:  ##하루더 올라갔다 내려갔다를 반복해야하면
        day = 1
    day += (height - up)//dn + 1
    print(day)

##겉으로 보면 되게 쉬워보이는데 꽤 헤맸던 문제다.
##포인트는 달팽이가 마지막에는 up보다 같거나 작은 거리를 이동해서 올라가야한다는 것
##그 포인트만 잡았으면 쉽게 풀 수 있었던 문제. 너무 어렵게 생각했다/