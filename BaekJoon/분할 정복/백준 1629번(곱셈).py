##함수 선언 부분
def mult(A, B, C):
    if B == 1:
        return A % C

    ans = mult(A, B//2, C)
    if B % 2 == 0:
        return ans ** 2 % C
    else:
        return ans ** 2 * A % C


##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(mult(A, B, C))

 ##(a * b) % c = ((a % c) * (b % c)) %c임을 몰랐다면 풀기 어려웠던 문제