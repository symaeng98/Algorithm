##함수 선언 부분##


##변수 선언 부분##


##메인 함수 부분##
if __name__ == "__main__":
    array = [7,5,9,0,3,1,6,2,4,8]

    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i] , array[min_index] = array[min_index], array[i] #swap

    print(array)
