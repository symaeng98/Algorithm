class MyMatrix:

    ##문제1번##
    def getNewMatrix(self, N):
        N_squared = N
        N_safe = N
        cnt = 0
        Matrix = [[0 for x in range(N)] for y in range(N)]
        while N_safe > 0:
            for i in range(cnt, N_safe + cnt):
                for j in range(cnt, N_safe + cnt):
                    if i == cnt or i == N_safe + cnt - 1 or j == cnt or j == N_safe + cnt - 1:
                        Matrix[i][j] = N_squared

            N_squared *= N
            cnt += 1
            N_safe -= 2
        return Matrix

    ##문제2번##
    def saveFileMatrix(self,M):
        cnt = 0
        str_M = str(M)
        with open("MATRIX.TXT",'a') as file1:
            file1.write("#LENGTH:%d#"%(len(M))+'\n')
            for i in range(len(str_M)):
                if str_M[i] != " ":
                    file1.write(str_M[i])
            file1.write('\n')

        with open("MATRIX.TXT",'r') as file1:
            For_cnt = file1.readlines()
            for i in For_cnt:
                if i.startswith("#"):
                    cnt += 1
        return cnt

    ##문제3번##
    def readFileMatrix(self,N):
        with open("MATRIX.TXT", "r") as file2:
            Read = file2.readlines()
            for Is_N in Read:
                if Is_N[8] == str(N): # #LENGTH:N#에서 N에 해당하는 인덱스
                    return MyMatrix.getNewMatrix(N)
            return -1

    ##문제4번##
    def readFileMaxValue(self):
        maxN = -1
        num = []
        sum = 0
        with open("MATRIX.TXT", "r") as file3:
            Read = file3.readlines()
            for is_N in Read:
                if is_N.startswith('['):
                    i = 2
                    while is_N[i]!=',':
                        num.append(is_N[i])
                        i+=1
                    j = 1
                    while len(num) != 0:
                        sum += int(num.pop())*j
                        j *= 10
                    if sum > maxN:
                        maxN = sum
                    sum = 0
                    i = 2
                    j = 1 #초기화
        print(maxN)
        return (maxN, maxN**(maxN//2+1))

    ##문제 5번##
    def __init__(self,N):
        N_squared = N
        N_safe = N
        cnt = 0
        Matrix = [[0 for x in range(N)] for y in range(N)]
        while N_safe > 0:
            for i in range(cnt, N_safe + cnt):
                for j in range(cnt, N_safe + cnt):
                    if i == cnt or i == N_safe + cnt - 1 or j == cnt or j == N_safe + cnt - 1:
                        Matrix[i][j] = N_squared

            N_squared *= N
            cnt += 1
            N_safe -= 2

        self.matrix = Matrix

    def __eq__(self, other):
        return self.matrix == other.matrix
    def __ne__(self, other):
        return self.matrix != other.matrix

    ##문제7번##
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return -1
        else:
            length = len(self.matrix)
            newmatrix = [[0]*length for y in range(length)]
            for i in range(length):
                for j in range(length):
                    newmatrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

            return newmatrix


    ##문제6번##
    def applyGivenFunction(self,fn):
        length = len(self.matrix)
        for i in range(length):
            for j in range(length):
                self.matrix[i][j] = fn(self.matrix[i][j])

        return self.matrix

def khs(N):
    return N + 3


##문제8번##
class MyDerivedMatrix(MyMatrix):

    def getMemberMatrix(self):
        return self.matrix









if __name__ == "__main__":
    N = int(input())

    # ---------문제1번---------#
    # M = MyMatrix()
    # Matrix = M.getNewMatrix(N)
    # print(Matrix)

    # ---------문제2번---------#
    # cnt = M.saveFileMatrix(Matrix)
    # print(cnt)

    # ---------문제3번---------#
    # Matrix2 = M.readFileMatrix(N)
    # print(Matrix2)

    # ---------문제4번---------#
    # max2 = M.readFileMaxValue()
    # print(max2)

    # ---------문제5번,7번---------#
    # M2 = MyMatrix(N)
    # M3 = MyMatrix(N)
    # print(M2 == M3)
    # print(M2.__eq__(M3))
    # print(M2+M3)

    # ---------문제6번---------#
    # M4 = MyMatrix(N)
    # M5 = M4.applyGivenFunction(khs)
    # print(M5)

    # ---------문제8번---------#
    M6 = MyDerivedMatrix(N+2)
    M7 = MyMatrix(N)
    print(M6.matrix)
