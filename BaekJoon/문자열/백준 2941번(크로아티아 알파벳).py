##함수 선언 부분##

##변수 선언 부분##
Str = []
##메인 함수 부분##
if __name__ == "__main__" :
    Str = input()
    Str = Str.replace('c=','1')  ##단어를 1로 바꾼다
    Str = Str.replace('c-', '1')
    Str = Str.replace('dz=', '1')
    Str = Str.replace('d-', '1')
    Str = Str.replace('lj', '1')
    Str = Str.replace('nj', '1')
    Str = Str.replace('s=', '1')
    Str = Str.replace('z=', '1')

    print("%d"%len(Str)) ##길이가 1의 개수이자 알파벳의 개수

##파이썬이기에 쉬웠던 문제
##엄청난 꼼수로 쉽게 풀 수 있지만 다르게 해결하려면 count 함수를 이용하는 정도?