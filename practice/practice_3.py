##함수 선언 부분

##변수 선언 부분##

##메인 함수 실행 부분##
if __name__=="__main__":

    myList=[30,10,20]
    print("현재 리스트 : %s" %myList)

    myList.append(40)
    print("append(40)후의 리스트 : %s" %myList)

    print("pop()으로 추출한 값 : %s" %myList.pop())
    print("pop()후의 리스트 : %s" %myList)

    myList.sort()
    print("sort()후의 리스트 : %s" %myList)

    myList.reverse()
    print("reverse후의 리스트 : %s" %myList)

    print("20값의 위치 : %d" %myList.index(20))

    myList.insert(2,222)
    print("insert(2,222)후의 리스트 : %s"%myList)

    myList.remove(222)
    print("remove(222)후의 리스트 : %s"%myList)

    myList.extend([77,88,77])
    print("extend([77,88,77])후의 리스트 : %s"%myList)
    
    myList+=[100,200,300]
    print(myList)
    
    print("77값의 개수 : %d" %myList.count(77))

    print("리스트의 개수는 %d개"%len(myList))

    
