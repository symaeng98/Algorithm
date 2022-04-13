##변수 선언 부분##
Num1 = []
Num2 = []
Str = []
NewStr = []
len1 = 0
len2 = 0
List1 = []
List2 = []
##메인 함수 부분##
if __name__ == "__main__":
    Str = input()
    NewStr = Str.split()
    len1 = len(NewStr[0])
    len2 = len(NewStr[1])
    Num1 = NewStr[0]
    Num2 = NewStr[1]
    for i in range(0, len1):
        List1.append(Num1[len1-i-1])
    for i in range(0, len2):
        List2.append(Num2[len2-i-1])
    if(List1[0]>List2[0]) :
        for i in range(0, 3):
            print(List1[i],end="")
    elif(List1[0]<List2[0]):
        for i in range(0, 3):
            print(List2[i],end="")
    else:
        if (List1[1] > List2[1]):
            for i in range(0, 3):
                print(List1[i], end="")
        elif (List1[1] < List2[1]):
            for i in range(0, 3):
                print(List2[i], end="")
        else:
            if (List1[2] > List2[2]):
                for i in range(0, 3):
                    print(List1[i], end="")
            else:
                for i in range(0, 3):
                    print(List2[i], end="")

##그닥 의미가 있어보이진 않는 문제다. 조건문을 계속 돌려주면 풀리는 문제
##파이썬이기 때문에 쉽게 풀었던 문제였던 것 같다.
