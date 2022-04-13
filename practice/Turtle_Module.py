import random
from tkinter.simpledialog import *
##함수 선언 부분
def getString():
    retStr = ''
    retStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return retStr

def getRGB() :
    r,g,b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
def getXYAS(sw,sh) :
    x, y, angle, size = 0, 0, 0, 0
    x = random.randrange(-sw/2, sw/2)
    y = random.randrange(-sh/2, sh/2)
    angle = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return [x, y, angle, size]
##변수 선언 부분##
lotto = []
num = 0
##메인 함수 실행 부분##
if __name__ == "__main__":
    print("** 로또 추첨을 시작합니다. **\n");

    while True :
        num = getNumber()

        if lotto.count(num) == 0:
            lotto.append(num)
        if len(lotto) >= 6:
            break

    print("추첨된 로또 번호 ==> ", end="")
    lotto.sort()
    for i in range(0, 6):
        print("%d " %lotto[i], end="")