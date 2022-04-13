##함수 선언 부분##
def quick_sort(array, start, end):
    if start >= end: #원소 개수가 1개인 경우
        return
    pivot = start #첫 번째 원소가 피벗
    left = start + 1
    right = end
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            #left가 end보다 커지거나 array[left]값이 피벗보다 큰 값을 찾으면 탈출한다.
            left += 1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            #right가 피벗과 같거나 작아지거나 array[right]가 피벗보다 작은 값을 찾으면 탈출한다.
            right -= 1
        if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체한다.
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체한다.
            array[left], array[right] = array[right], array[left]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행한다.
    quick_sort(array, start, right - 1) #현재 right의 위치에 피벗이 위치한다.
    quick_sort(array, right + 1, end)
##변수 선언 부분##

##메인 함수 부분##
if __name__ == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    quick_sort(array, 0, len(array)-1)
    print(array)